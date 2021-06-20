import datetime
from typing import List

day = datetime.date.today().strftime('%a')


def plugin_filter_day(days: List[str]):
    return day in days
