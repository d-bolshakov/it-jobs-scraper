from .ParsingResult import ParsingResult
from .utils.DateConverter import convertDate
from .utils.LocationExtractor import extractLocationsList
from .ParsedVacancy import ParsedVacancy
from bs4 import BeautifulSoup, Tag
import unicodedata


class DouParser:
    def parse(self, html: str, lastProcessedVacancyLink: str) -> ParsingResult:
        bs = BeautifulSoup(html, 'html.parser')
        vacancies, lastProcessedReached = self.parseVacanciesList(
            bs, lastProcessedVacancyLink)
        isMoreAvailable = self.isMoreAvailable(bs)
        csrfToken = self.getCSRFToken(bs) if isMoreAvailable else None
        return {'vacancies': vacancies, 'isMoreAvailable': isMoreAvailable, 'lastProcessedReached': lastProcessedReached, 'csrfToken': csrfToken}

    def parseVacanciesList(self, input: BeautifulSoup, lastProcessedVacancyLink: str) -> tuple[list[ParsedVacancy], bool]:
        lastProcessedReached = False
        vacancies_list = input.select('li.l-vacancy')
        vacancies: list[ParsedVacancy] = []
        for v in vacancies_list:
            if lastProcessedVacancyLink and v.select_one('a.vt')['href'] == lastProcessedVacancyLink:
                lastProcessedReached = True
                break
            vacancies.append(self.extractVacancyData(v))
        return vacancies, lastProcessedReached

    def extractVacancyData(self, v: Tag) -> ParsedVacancy:
        title = v.select_one(
            'div.title').select_one('a.vt').text
        company = unicodedata.normalize(
            'NFKD', v.select_one('a.company').text).strip()
        link = v.select_one('a.vt')['href']
        location = extractLocationsList(v.select_one(
            'span.cities').text.strip())
        publishedAt = convertDate(
            v.select_one('div.date').text)
        source = 'Dou'
        return {
            'title': title,
            'company': company,
            'link': link,
            'location': location,
            'publishedAt': publishedAt,
            'source': source
        }

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
