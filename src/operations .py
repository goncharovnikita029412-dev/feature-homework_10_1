from typing import List, Dict
from datetime import datetime

# Определение типа операции (по желанию)
Operation = Dict[str, any]

def filter_operations_by_status(operations: List[Operation], status: str) -> List[Operation]:
    """
    Фильтрует список операций по заданному статусу.
    
    Args:
        operations (List[Operation]): список операций.
        status (str): статус для фильтрации.
    
    Returns:
        List[Operation]: список операций, соответствующих статусу.
    """
    return [op for op in operations if op.get('status') == status]


def sort_operations_by_date(operations: List[Operation], reverse: bool = False) -> List[Operation]:
    """
    Сортирует список операций по дате.
    
    Args:
        operations (List[Operation]): список операций.
        reverse (bool): порядок сортировки, по убыванию (от новых к старым). По умолчанию False.
    
    Returns:
        List[Operation]: отсортированный список операций.
    """
    def parse_date(op):
        date_str = op.get('date')
        return datetime.fromisoformat(date_str)

    return sorted(operations, key=parse_date, reverse=reverse)