from typing import Protocol
from data.VacancyCategory import VacancyCategory


class VacancyFilters(Protocol):
    source: str | None
    years_of_expirience: float | None
    category: VacancyCategory
