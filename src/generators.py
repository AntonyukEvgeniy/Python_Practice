from collections.abc import Callable
from email.generator import Generator
from operator import index
from typing import Iterator

from tests.conftest import transactions


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """
    Создайте функцию
    filter_by_currency
    ,которая принимает на вход список словарей, представляющих транзакции.
    Функция должна возвращать итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD).
    """
    transactions_by_currency = list(
        filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions)
    )
    for tran in transactions_by_currency:
        yield tran


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """
    Генератор transaction_descriptions, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
    """
    for tran in transactions:
        yield tran["description"]


def card_number_generator(start:int, stop:int)-> Iterator[str]:
    """
        Создайте генератор
    card_number_generator
    , который выдает номера банковских карт в формате
    XXXX XXXX XXXX XXXX
    , где
    X
     — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор должен принимать начальное и конечное значения для генерации диапазона номеров.
    """
    credit_card_number = "0000000000000000"
    for n in range(start, stop+1, 1):
        change_len = 16 - len(str(n))
        credit_card_number_new = f"{credit_card_number[0:change_len]}{n}"
        credit_card_number_new_formatted = f"{credit_card_number_new[0:4]} {credit_card_number_new[4:8]} {credit_card_number_new[8:12]} {credit_card_number_new[12:]}"
        yield credit_card_number_new_formatted

for card_number in card_number_generator(1, 5):
    print(card_number)
