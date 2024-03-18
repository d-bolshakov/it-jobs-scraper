from dataclasses import dataclass


@dataclass
class Location:
    city: str
    country: str

    def asDict(self):
        return {
            'city': self.city,
            'country': self.country,
        }
