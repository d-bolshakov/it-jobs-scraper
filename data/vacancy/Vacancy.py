from datetime import date, datetime
from dataclasses import dataclass
from data.vacancy.VacancyCategory import VacancyCategory
from data.location.Location import Location


@dataclass
class Vacancy:
    title: str
    company: str
    location: list[Location]
    link: str
    publishedAt: date
    source: str
    category: VacancyCategory
    # years_of_experience: float
    scrapedAt: datetime = datetime.now()

    def asDict(self) -> dict:
        return {
            'title': self.title,
            'company': self.company,
            'location': [location.asDict() for location in self.location],
            'link': self.link,
            'publishedAt': self.publishedAt.strftime('%Y-%m-%d'),
            'source': self.source,
            'category': self.category.value,
            'scrapedAt': self.scrapedAt.isoformat(),
        }
