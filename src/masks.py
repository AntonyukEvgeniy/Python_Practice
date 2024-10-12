import logging
from typing import Union

from src.decorators import log

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/masks.log", mode="w")
logger.addHandler(file_handler)
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.setLevel(logging.DEBUG)


@log("mylog.txt")
def get_mask_card_number(card_number: Union[str, int]) -> str:
    """
    Принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате:
    XXXX XX** **** XXXX
    """
    card_text_view = str(card_number)
    if not card_text_view.isdigit():
        logger.error("Произошла ошибка: Неверный формат номера карты")
        raise ValueError("Неверный формат номера карты")

    if len(card_text_view) != 16:
        logger.error("Произошла ошибка: Неверный формат номера карты")
        raise ValueError("Неверный формат номера карты")
    card_formated_view = f"{card_text_view[0:4]} {card_text_view[4:6]}** **** {card_text_view[-4:]}"
    logger.debug(f"Карта {card_text_view} замаскирована, результат: {card_formated_view}")
    return card_formated_view


@log()
def get_mask_account(bank_account_number: Union[str, int]) -> str:
    """
    Принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается в формате
    **XXXX
    """
    bank_account_text_view = str(bank_account_number)
    if not bank_account_text_view.isdigit():
        logger.error("Произошла ошибка: Введен неверный номер счета")
        raise ValueError("Введен неверный номер счета")
    bank_account_formated = f"**{bank_account_text_view[-4:]}"
    logger.debug(f"Номер счета {bank_account_text_view} замаскирован, результат: {bank_account_formated}")
    return bank_account_formated
