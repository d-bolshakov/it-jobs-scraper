from typing import TypedDict
from data.location.Location import Location
from datetime import date


class ParsedVacancy(TypedDict):
    title: str
    company: str
    link: str
    location: list[Location]
    publishedAt: date
    source: str
