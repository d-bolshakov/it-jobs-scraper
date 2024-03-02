from proxy.manager.ProxyManager import ProxyManager
from proxy.storage.ProxyStorage import ProxyStorage

storage = ProxyStorage()
manager = ProxyManager(storage)

print(manager.getProxy())
