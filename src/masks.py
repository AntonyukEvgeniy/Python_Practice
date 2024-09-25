from typing import Union

from src.decorators import log


@log("mylog.txt")
def get_mask_card_number(card_number: Union[str, int]) -> str:
    """
    Принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате:
    XXXX XX** **** XXXX
    """
    card_text_view = str(card_number)
    if not card_text_view.isdigit():
        raise ValueError("Неверный формат номера карты")
    if len(card_text_view) != 16:
        raise ValueError("Неверный формат номера карты")
    card_formated_view = f"{card_text_view[0:4]} {card_text_view[4:6]}** **** {card_text_view[-4:]}"
    return card_formated_view


@log()
def get_mask_account(bank_account_number: Union[str, int]) -> str:
    """
    Принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается в формате
    **XXXX
    """
    bank_account_text_view = str(bank_account_number)
    if not bank_account_text_view.isdigit():
        raise ValueError("Введен неверный номер счета")
    bank_account_formated = f"**{bank_account_text_view[-4:]}"
    return bank_account_formated
