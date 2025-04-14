from typing import List, Dict, Any


def filter_by_state(operations: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """ Функция принимает список словарей и опционально значение для ключа 'state'. По умолчанию state == EXECUTED """

    return [item for item in operations if item.get("state") == state]


def sort_by_date(operations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Функция принимает список словарей и параметр, задающий порядок сортировки (по умолчанию — убывание)"""

    return sorted(operations, key=lambda item: item["date"], reverse = True)


print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]))

print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]))
