from datetime import datetime as dt

from .filter_utils import parse_list

DAYS = [str(x) for x in range(1, 32)]
MONTHS = [str(x) for x in range(1, 13)]

day = dt.today()
FORMAT = '%Y-%m-%d'


def plugin_filter_repeat(from_date: str = None, to_date: str = None,
                         days: int = None, months: int = None):
    result = True
    if from_date is not None:
        result = result and (day > parse_date(from_date))

    if to_date is not None:
        result = result and (day < parse_date(to_date))

    if days is not None:
        result = result and (day.strftime('%d').replace(
            '0', '') in parse_list(days, DAYS))

    if months is not None:
        result = result and (day.strftime('%m').replace(
            '0', '') in parse_list(months, MONTHS))

    return result


def parse_date(date_str: str) -> dt:
    return dt.strptime(date_str, FORMAT)
