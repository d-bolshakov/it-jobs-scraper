from datetime import date, datetime
from dataclasses import dataclass
from data.VacancyCategory import VacancyCategory


@dataclass
class Vacancy:
    title: str
    company: str
    location: str
    link: str
    publishedAt: date
    source: str
    # category: VacancyCategory
    # years_of_experience: float
    scrapedAt: datetime = datetime.now()

    def asDict(self) -> dict:
        return {
            'title': self.title,
            'company': self.company,
            'location': self.location,
            'link': self.link,
            'publishedAt': self.publishedAt.strftime('%Y-%m-%d'),
            'source': self.source,
            'scrapedAt': self.scrapedAt.isoformat(),
        }
