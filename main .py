# main.py

from src.operations import filter_operations_by_status, sort_operations_by_date

# пример массива операций
operations = [
    {"status": "completed", "date": "2024-11-05T14:30:00"},
    {"status": "pending", "date": "2024-11-07T09:15:00"},
    {"status": "failed", "date": "2024-11-04T12:00:00"},
    {"status": "completed", "date": "2024-11-08T10:00:00"},
]

# фильтрация по статусу "completed"
completed_ops = filter_operations_by_status(operations, "completed")
print("Завершенные операции:")
for op in completed_ops:
    print(op)

# сортировка по дате (от новых к старым)
sorted_ops = sort_operations_by_date(operations, reverse=True)
print("\nОперации отсортированы по дате (от новых к старым):")
for op in sorted_ops:
    print(op)