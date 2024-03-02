from proxy.manager.AbstractProxyManager import AbstractProxyManager
from ..shared.ScrapingTask import ScrapingTask
from repositories.vacancy.AbstractVacancyRepository import AbstractVacancyRepository
from data.Vacancy import Vacancy
from .DouTaskRootUrlBuilder import DouTaskRootUrlBuilder
from .DouParser import DouParser
import requests
from operator import itemgetter


class DouScraper:
    def __init__(self, proxyManager: AbstractProxyManager, vacancyRepo: AbstractVacancyRepository):
        self.proxyManager = proxyManager
        self.vacancyRepo = vacancyRepo
        self.tasks = []
        self.parser = DouParser()

    def registerTask(self, task: ScrapingTask):
        self.tasks.append(task)

    def runTask(self, task: ScrapingTask):
        lastProcessedVacancy = self.vacancyRepo.getLastProcessedVacancy({
                                                                        'source': 'Dou'})
        rootUrl = DouTaskRootUrlBuilder(task)
        session = requests.session()
        proxy = self.proxyManager.getProxy()
        res = session.get(rootUrl, proxies={'http': proxy}, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'})
        vacancies, isMoreAvailable, lastProccesedReached, csrfToken = itemgetter('vacancies', 'isMoreAvailable', 'lastProcessedReached', 'csrfToken')(self.parser.parse(
            res.text, lastProcessedVacancy))
        url = rootUrl.replace('/vacancies/', '/vacancies/xhr-load/')
        while isMoreAvailable and not lastProccesedReached:
            res = session.post(url, {'csrfmiddlewaretoken': csrfToken, 'count': len(vacancies)}, proxies={'http': proxy}, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Referer': rootUrl}).json()
            newVacancies, lastProccesedReached = itemgetter('vacancies', 'lastProcessedReached')(self.parser.parse(
                res['html'], lastProcessedVacancy))
            vacancies += newVacancies
            isMoreAvailable = not res['last']
        for vacancy in vacancies:
            self.vacancyRepo.save(vacancy)
        return
