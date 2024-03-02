from proxy.storage.ProxyStorage import ProxyStorage
from proxy.manager.ProxyManager import ProxyManager
from scrapers.shared.ScrapingTask import ScrapingTask
from data.VacancyCategory import VacancyCategory
from scrapers.dou.DouScraper import DouScraper
from repositories.vacancy.JsonVacancyRepository import JsonVacancyRepository

proxyStorage = ProxyStorage()
proxyManager = ProxyManager(proxyStorage)

vacancyRepo = JsonVacancyRepository()

douScraper = DouScraper(proxyManager, vacancyRepo)

pythonCategory = VacancyCategory.PYTHON
pythonTask = ScrapingTask(pythonCategory, 2)

douScraper.runTask(pythonTask)
