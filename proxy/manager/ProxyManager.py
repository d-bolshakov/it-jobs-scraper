import requests
import random
from ..storage.AbstractProxyStorage import AbstactProxyStorage
from .AbstractProxyManager import AbstractProxyManager


class ProxyManager(AbstractProxyManager):
    proxies: list[str] = []
    storage: AbstactProxyStorage

    def __init__(self, storage: AbstactProxyStorage) -> None:
        self.storage = storage
        self.loadProxiesList()

    def loadProxiesList(self) -> None:
        proxies = self.storage.getList()
        if not proxies:
            return self.updateProxiesList()
        self.proxies = proxies

    def fetchProxiesList(self) -> list[str]:
        response = requests.get(
            'https://proxylist.geonode.com/api/proxy-list?limit=100&page=1&sort_by=lastChecked&sort_type=desc')
        proxies = []
        for proxy in response.json()['data']:
            if proxy['country'] != 'RU':
                proxies.append(proxy['ip'] + ':' + proxy['port'])
        return proxies

    def updateProxiesList(self) -> None:
        newProxiesList = self.fetchProxiesList()
        self.proxies = newProxiesList
        self.storage.saveList(newProxiesList)

    def getProxy(self) -> str:
        if len(self.proxies) == 0:
            self.updateProxiesList()
        return random.choice(self.proxies)

    def reportInvalidProxy(self, proxy: str) -> None:
        self.proxies.remove(proxy)
        self.storage.removeItem(proxy)
