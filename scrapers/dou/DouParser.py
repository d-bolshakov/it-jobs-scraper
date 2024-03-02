from .ParsingResult import ParsingResult
from data.Vacancy import Vacancy
from .utils.DateConverter import convertDate
from bs4 import BeautifulSoup
import unicodedata


class DouParser:
    def parse(self, html: str, lastProcessed: Vacancy) -> ParsingResult:
        bs = BeautifulSoup(html, 'html.parser')
        vacancies, lastProcessedReached = self.parseVacanciesList(
            bs, lastProcessed)
        isMoreAvailable = self.isMoreAvailable(bs)
        csrfToken = self.getCSRFToken(bs) if isMoreAvailable else None
        return {'vacancies': vacancies, 'isMoreAvailable': isMoreAvailable, 'lastProcessedReached': lastProcessedReached, 'csrfToken': csrfToken}

    def parseVacanciesList(self, input: BeautifulSoup, lastProcessedVacancy: Vacancy) -> tuple[list[Vacancy], bool]:
        lastProcessedReached = False
        vacancies_list = input.select('li.l-vacancy')
        vacancies: list[Vacancy] = []
        for v in vacancies_list:
            if lastProcessedVacancy and v.select_one('a.vt')['href'] == lastProcessedVacancy['link']:
                lastProcessedReached = True
                break
            vacancy = Vacancy(title=v.select_one(
                'div.title').select_one('a.vt').text, company=unicodedata.normalize(
                'NFKD', v.select_one('a.company').text).strip(), link=v.select_one('a.vt')['href'], location=v.select_one(
                'span.cities').text.strip(), publishedAt=convertDate(
                v.select_one('div.date').text), source='Dou')
            vacancies.append(vacancy)
        return vacancies, lastProcessedReached

    def isMoreAvailable(self, input: BeautifulSoup) -> bool:
        moreButtonDiv = input.select_one('div.more-btn')
        if not moreButtonDiv:
            return False
        return True

    def getCSRFToken(self, input: BeautifulSoup) -> str:
        scripts = input.find_all('script')
        scripts = [script.text for script in scripts]
        csrfToken = ''
        for script in scripts:
            if 'window.CSRF_TOKEN =' in script:
                csrfToken = script.split('window.CSRF_TOKEN = "')[
                    1].split('"')[0]
        return csrfToken
