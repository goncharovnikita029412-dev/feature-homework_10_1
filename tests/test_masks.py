def test_get_mask_account():
    assert get_mask_account("1234567890123456") == "**3456"
    assert get_mask_account("000012345678") == "**678"
import pytest
from src.masks.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    # тест с пробелами
    assert get_mask_card_number("7000 79 22 89 6063 61") == "7000 79** **** 6361"


