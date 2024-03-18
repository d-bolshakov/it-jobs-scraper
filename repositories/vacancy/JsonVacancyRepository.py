from data.vacancy.Vacancy import Vacancy
from repositories.vacancy.VacancyFilters import VacancyFilters
from .AbstractVacancyRepository import AbstractVacancyRepository
import os
from pysondb import getDb


class JsonVacancyRepository(AbstractVacancyRepository):
    def __init__(self) -> None:
        self.filePath = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), 'vacancies.json')
        self.db = getDb(self.filePath, log=True)

    def save(self, vacancy: Vacancy) -> None:
        self.db.add(vacancy.asDict())

    def getLastProcessedVacancy(self, filters: VacancyFilters) -> Vacancy | None:
        vacancies = self.db.getByQuery({'source': filters['source']})
        if len(vacancies) == 0:
            return None
        vacancies = sorted(
            vacancies, key=lambda vacancy: vacancy['scrapedAt'], reverse=True)
        return vacancies[0]
