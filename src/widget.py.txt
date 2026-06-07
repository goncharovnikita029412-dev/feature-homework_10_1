from masks.masks import get_mask_card_number, get_mask_account
from datetime import datetime

def mask_account_card(s: str) -> str:
    parts = s.strip().split()
    if len(parts) < 2:
        raise ValueError("Строка должна содержать тип и номер")
    type_ = parts[0]
    number = parts[-1]
    if type_.lower() == 'счет':
        return f"Счет {get_mask_account(number)}"
    else:
        return f"{type_} {get_mask_card_number(number)}"

def get_date(date_str: str) -> str:
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")