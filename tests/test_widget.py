import pytest

from src.widget import mask_account_card


@pytest.mark.parametrize(
    "user_pay_info,expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199","Maestro 1596 83** **** 5199"),
        ("Visa Gold 5999414228426353","Visa Gold 5999 41** **** 6353"),
        ("Счет 64686473678894779589","Счет **9589"),
        ("Счет 64686","Счет **4686")

    ],
)
def test_mask_account_card(user_pay_info, expected):
    assert mask_account_card(user_pay_info) == expected

def test_mask_account_card_wrong_format():
    user_pay_info = "Cxtn"
    with pytest.raises(ValueError,match="Введены некорректные данные"):
        mask_account_card(user_pay_info)