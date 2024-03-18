from .AbstractVacancyRepository import AbstractVacancyRepository
from data.vacancy.Vacancy import Vacancy
from data.vacancy.VacancyCategory import VacancyCategory
from .VacancyFilters import VacancyFilters
import os
import json
from pathlib import Path


class LocalVacancyRepository(AbstractVacancyRepository):
    def __init__(self) -> None:
        self.filePath = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), 'vacancies.json')

    def save(self, vacancy: Vacancy) -> None:
        with open(self.filePath, 'w+') as vacanciesListFile:
            vacancies = []
            vacancies = json.load(vacanciesListFile)
            vacancies.append(vacancy)
            json.dump([vacancy.asDict()
                      for vacancy in vacancies if type(vacancy) == Vacancy], vacanciesListFile, indent=2)

    # def getById(self, id: int) -> Vacancy | None:
    #     if not os.path.isfile(self.filePath) or os.path.getsize(self.filePath) == 0:
    #         return None
    #     with open(self.filePath) as vacanciesListFile:
    #         vacancies = json.loads(vacanciesListFile.read())
    #         return (vacancy for vacancy in vacancies if vacancy.id == id) | None

    def getLastProcessedVacancy(self, filters: VacancyFilters) -> Vacancy | None:
        if not os.path.isfile(self.filePath) or os.path.getsize(self.filePath) == 0:
            return None
        with open(self.filePath) as vacanciesListFile:
            vacancies = json.load(vacanciesListFile)
        if len(vacancies) == 0:
            return None
        filteredVacancies: list[Vacancy] = []
        # for vacancy in vacancies:
        #     # if filters.category and vacancy.category != filters.category:
        #     #     continue
        #     if filters.source and vacancy.source != filters.source:
        #         continue
        #     # if filters.years_of_expirience and vacancy.years_of_experience != filters.years_of_expirience:
        #     #     continue
        #     filteredVacancies.append(vacancy)
        # vacancies = [
        #     vacancy for vacancy in vacancies if vacancy.source == source and vacancy.category == category.value]
        vacancies = sorted(
            vacancies, key=lambda vacancy: vacancy['scrapedAt'], reverse=True)
        return vacancies[0]
