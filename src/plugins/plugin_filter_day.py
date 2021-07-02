import datetime

from .filter_utils import parse_list

day = datetime.date.today().strftime('%a')

DAYS = [
    'Mon',
    'Tue',
    'Wed',
    'Thu',
    'Fri',
    'Sat',
    'Sun'
]


def plugin_filter_day(days: str) -> bool:
    """Содержится ли текущий день недели в полученном списке"""
    days_list = parse_list(days, DAYS)

    return day in days_list
