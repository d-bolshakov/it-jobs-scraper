from ..shared.ScrapingTask import ScrapingTask
from .mappings.CategoryLinks import CATEGORY_LINKS


def DouTaskRootUrlBuilder(task: ScrapingTask) -> str:
    url = CATEGORY_LINKS[task.category] if task.category in CATEGORY_LINKS else None
    if not url:
        raise KeyError(
            f'URL mapping for category {task.category} does not exist')

    match task.years_of_experience:
        case num if 0 <= num <= 1:
            url += '&exp=0-1'

        case num if 1 < num <= 3:
            url += '&exp=1-3'

        case num if 3 < num <= 5:
            url += '&exp=3-5'

        case num if num > 5:
            url += '&exp=5plus'

    return url
