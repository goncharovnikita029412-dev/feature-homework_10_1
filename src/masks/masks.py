from typing import str

def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты по формату: XXXX XX** **** XXXX
    показываются первые 6 и последние 4 цифры.
    """
    # убираем все пробелы и другие нецифровые символы
    digits = ''.join(filter(str.isdigit, card_number))
    if len(digits) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")
    return f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"

def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета в формате: **XXXX.
    """
    digits = ''.join(filter(str.isdigit, account_number))
    if len(digits) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 цифры")
    return f"**{digits[-4:]}"
