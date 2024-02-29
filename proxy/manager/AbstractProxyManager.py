from abc import ABC, abstractmethod


class AbstractProxyManager(ABC):

    @abstractmethod
    def getProxy(self) -> str:
        pass

    @abstractmethod
    def reportInvalidProxy(self, proxy: str) -> None:
        pass
