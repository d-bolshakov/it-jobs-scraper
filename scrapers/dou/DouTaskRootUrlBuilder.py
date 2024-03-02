from data.VacancyCategory import VacancyCategory
from ..shared.ScrapingTask import ScrapingTask


def DouTaskRootUrlBuilder(task: ScrapingTask) -> str | None:
    url = ''
    match task.category:
        case VacancyCategory.FRONT_END:
            url = 'https://jobs.dou.ua/vacancies/?category=Front%20End'

        case VacancyCategory.NODE:
            url = 'https://jobs.dou.ua/vacancies/?category=Node.js'

        case VacancyCategory.PYTHON:
            url = 'https://jobs.dou.ua/vacancies/?category=Python'

        case _:
            return None

    match task.years_of_experience:
        case num if 0 <= num <= 1:
            url += '&exp=0-1'

        case num if 1 < num <= 3:
            url += '&exp=1-3'

        case num if 3 < num <= 5:
            url += '&exp=3-5'

        case num if num > 5:
            url += '&exp=5plus'

    return url
