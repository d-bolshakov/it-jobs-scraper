from data.VacancyCategory import VacancyCategory


class ScrapingTask:
    def __init__(self, category: VacancyCategory, years_of_experience: float) -> None:
        self.category = category
        self.years_of_experience = years_of_experience
