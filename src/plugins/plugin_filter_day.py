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

# Mon,Wed-Fri for ['Mon', 'Wed', 'Thu', 'Fri']
def parse_days(days: str):
    chunks = days.split(',')
    days_list = []

    for chunk in chunks:
        if '-' in chunk:
            start, end = chunk.split('-')

            days_list += DAYS[DAYS.index(start): DAYS.index(end) + 1]
        else:
            days_list.append(chunk)

    return days_list


def plugin_filter_day(days: str):
    days_list = parse_days(days)

    return day in days_list
