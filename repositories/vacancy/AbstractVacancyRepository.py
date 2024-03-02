from abc import ABC, abstractmethod
from data.Vacancy import Vacancy
from .VacancyFilters import VacancyFilters


class AbstractVacancyRepository(ABC):

    @abstractmethod
    def save(self, vacancy: Vacancy) -> None:
        pass

    # @abstractmethod
    # def getById(self, id: int) -> Vacancy | None:
    #     pass

    @abstractmethod
    def getLastProcessedVacancy(self, filters: VacancyFilters) -> Vacancy | None:
        pass
