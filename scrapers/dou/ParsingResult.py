from typing import Protocol
from .ParsedVacancy import ParsedVacancy


class ParsingResult(Protocol):
    vacancies: list[ParsedVacancy]
    isMoreAvailable: bool
    lastProcessedReached: bool
    csrfToken: str | None
