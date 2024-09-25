from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """
    Принимает на вход список словарей, представляющих транзакции.
    Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD).
    """
    transactions_by_currency = list(
        filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions)
    )
    if len(transactions_by_currency) == 0:
        yield {}
    for tran in transactions_by_currency:
        yield tran


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """
    Генератор transaction_descriptions, который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди.
    """
    if len(transactions) == 0:
        yield "Нет транзакций"
    for tran in transactions:
        yield tran["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX, где X
     — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор должен принимать начальное и конечное значения для генерации диапазона номеров.
    """
    if start < 1 or start > 9999999999999999 or stop < 1 or stop > 9999999999999999 or stop < start:
        raise ValueError("Невозможный диапазон номера карты")
    credit_card_number = "0000000000000000"
    for n in range(start, stop + 1, 1):
        change_len = 16 - len(str(n))
        credit_card_number_new = f"{credit_card_number[0:change_len]}{n}"
        credit_card_number_new_formatted = (f"{credit_card_number_new[0:4]} {credit_card_number_new[4:8]}"
                                            f" {credit_card_number_new[8:12]} {credit_card_number_new[12:]}")
        yield credit_card_number_new_formatted
