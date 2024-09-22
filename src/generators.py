from operator import index

from tests.conftest import transactions


def filter_by_currency(transactions: list[dict], currency: str) -> iter:
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


def transaction_descriptions(transactions: list[dict]) -> iter:
    """
    Генератор transaction_descriptions, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
    """
    for tran in transactions:
        yield tran["description"]


def card_number_generator(start, end):
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
    credit_cards = []
    credit_card_number = "0000000000000000"
    for n in range(start, end+1, 1):
        change_len = 16 - len(str(n))
        credit_card_number_new = f"{credit_card_number[1:change_len]}{n}"

        credit_cards.append(credit_card_number_new)
    return credit_cards


print(card_number_generator(1,5))