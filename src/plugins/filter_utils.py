from typing import List


def parse_list(days: str, origin_list: list) -> List[str]:
    """
    Конвертирует строку вида 'Mon,Wed-Fri' в список
    вида '['Mon', 'Wed', 'Thu', 'Fri']'
    """
    if days == 'any':
        return origin_list

    chunks = days.split(',')
    days_list = []

    for chunk in chunks:
        if '-' in chunk:
            start, end = chunk.split('-')

            days_list += origin_list[origin_list.index(
                start): origin_list.index(end) + 1]
        else:
            days_list.append(chunk)

    return days_list
