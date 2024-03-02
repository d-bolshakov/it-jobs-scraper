import requests
from bs4 import BeautifulSoup
import unicodedata
from proxy.storage import ProxyStorage
from proxy.manager import ProxyManager

proxyStorage = ProxyStorage()
proxyManager = ProxyManager(proxyStorage)

url = 'https://jobs.dou.ua/vacancies/?category=Node.js'

res = requests.get(url, proxies={'http': next(proxyManager.getProxyGenerator())}, headers={
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'})

bs = BeautifulSoup(res.text, 'html.parser')
vacancies_div = bs.select_one('#vacancyListId')
vacancies_list = vacancies_div.find_all(['li'])
vacancies = [{
    'date': vacancy.select_one('div.date').text,
    'title': vacancy.select_one('div.title').select_one('a.vt').text,
    'link': vacancy.select_one('a.vt')['href'],
    'company': unicodedata.normalize('NFKD', vacancy.select_one('a.company').text).strip(),
    'location': vacancy.select_one('span.cities').text.strip()
}
    for vacancy in vacancies_list]
print(vacancies)
