import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "card_number,expected",
    [
        (2202208131326309, "2202 20** **** 6309"),
        (1111222233334444, "1111 22** **** 4444"),
        ("0000000000000000", "0000 00** **** 0000"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_wrong_format():
    card_number = "2202208131326309A"
    with pytest.raises(ValueError, match="Неверный формат номера карты"):
        get_mask_card_number(card_number)


def test_get_mask_card_number_wrong_len():
    card_number = "2202208131326309999"
    with pytest.raises(ValueError, match="Неверный формат номера карты"):
        get_mask_card_number(card_number)


@pytest.mark.parametrize(
    "bank_account_number,expected", [("73654108430135874305", "**4305"), ("00000000000000000000000000", "**0000")]
)
def test_get_mask_account(bank_account_number, expected):
    assert get_mask_account(bank_account_number) == expected


def test_get_get_mask_account_wrong_format():
    bank_account_number = "2202208131326309A"
    with pytest.raises(ValueError, match="Введен неверный номер счета"):
        get_mask_account(bank_account_number)
