from typing import Protocol
from data.Vacancy import Vacancy


class ParsingResult(Protocol):
    vacancies: list[Vacancy]
    isMoreAvailable: bool
    lastProcessedReached: bool
    csrfToken: str | None
