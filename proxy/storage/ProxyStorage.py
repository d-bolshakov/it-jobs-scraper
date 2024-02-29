import os
import json
from .AbstractProxyStorage import AbstactProxyStorage


class ProxyStorage(AbstactProxyStorage):

    def __init__(self) -> None:
        self.filePath = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), 'proxies.json')

    def getList(self) -> list[str] | None:
        if not os.path.isfile(self.filePath) or os.path.getsize(self.filePath) == 0:
            return None
        with open(self.filePath) as proxiesListFile:
            return json.loads(proxiesListFile.read())

    def saveList(self, proxiesList: list[str]) -> None:
        with open(self.filePath, 'w') as proxiesListFile:
            json.dump(proxiesList, proxiesListFile, indent=2)

    def removeItem(self, item: str) -> None:
        proxiesList = self.getList()
        if not item in proxiesList:
            return None
        proxiesList.remove(item)
        with open(self.filePath, 'w') as proxiesListFile:
            json.dump(proxiesList, proxiesListFile, indent=2)
