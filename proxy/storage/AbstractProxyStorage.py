from abc import ABC, abstractmethod


class AbstactProxyStorage(ABC):

    @abstractmethod
    def getList(self) -> list[str] | None:
        pass

    @abstractmethod
    def saveList(self, proxiesList: list[str]) -> None:
        pass

    @abstractmethod
    def removeItem(self, item: str) -> None:
        pass
