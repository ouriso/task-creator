from datetime import date, datetime

from .filter_utils import parse_list

DAYS = [str(x) for x in range(1, 32)]
MONTHS = [str(x) for x in range(1, 13)]

FORMAT = '%Y-%m-%d'


def plugin_filter_date(from_date: str = None, to_date: str = None,
                       days: int = None, months: int = None) -> bool:

    day = date.today()

    result = True

    if from_date is not None:
        result = result and (day >= parse_date(from_date))

    if to_date is not None:
        result = result and (day <= parse_date(to_date))

    if days is not None:
        result = result and ('{}'.format(day.day) in parse_list(days, DAYS))

    if months is not None:
        result = result and ('{}'.format(day.month)
                             in parse_list(months, MONTHS))

    return result


def parse_date(date_str: str) -> date:
    return datetime.strptime(date_str, FORMAT).date()
