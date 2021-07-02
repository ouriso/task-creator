import datetime
from typing import List

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


def parse_days(days: str) -> List[str]:
    """
    Конвертирует строку вида 'Mon,Wed-Fri' в список
    вида '['Mon', 'Wed', 'Thu', 'Fri']'
    """
    if days == 'any':
        return DAYS

    chunks = days.split(',')
    days_list = []

    for chunk in chunks:
        if '-' in chunk:
            start, end = chunk.split('-')

            days_list += DAYS[DAYS.index(start): DAYS.index(end) + 1]
        else:
            days_list.append(chunk)

    return days_list


def plugin_filter_day(days: str) -> bool:
    """Содержится ли текущий день недели в полученном списке"""
    days_list = parse_days(days)

    return day in days_list
