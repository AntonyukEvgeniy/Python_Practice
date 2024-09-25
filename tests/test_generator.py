import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(test_transactions, currency="USD"):
    gen = filter_by_currency(test_transactions, currency)
    assert next(gen) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(gen) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(gen) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }


def test_filter_by_currency_no_currency(test_transactions, currency="EUR"):
    gen = filter_by_currency(test_transactions, currency)
    assert next(gen) == {}


def test_filter_by_currency_empty(empty_transactions, currency="USD"):
    gen = filter_by_currency(empty_transactions, currency)
    assert next(gen) == {}


def test_transaction_descriptions(test_transactions):
    gen = transaction_descriptions(test_transactions)
    assert next(gen) == "Перевод организации"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "Перевод с карты на карту"
    assert next(gen) == "Перевод организации"


def test_transaction_descriptions_empty(empty_transactions):
    gen = transaction_descriptions(empty_transactions)
    assert next(gen) == "Нет транзакций"


card_numbers_expected_1 = [
    "0000 0000 0000 0001",
    "0000 0000 0000 0002",
    "0000 0000 0000 0003",
    "0000 0000 0000 0004",
    "0000 0000 0000 0005",
]
card_numbers_expected_2 = ["9999 9999 9999 9999"]
card_numbers_expected_3 = ["0000 0000 0000 0001"]


@pytest.mark.parametrize(
    "start,stop,expected",
    [
        (1, 5, card_numbers_expected_1),
        (9999999999999999, 9999999999999999, card_numbers_expected_2),
        (1, 1, card_numbers_expected_3),
    ],
)
def test_card_number_generator(start, stop, expected):
    generated_card_numbers = []
    for card_number in card_number_generator(start, stop):
        generated_card_numbers.append(card_number)
    assert generated_card_numbers == expected

def test_card_number_generator_error():
    gen = card_number_generator(56,55)
    with pytest.raises(ValueError, match="Невозможный диапазон номера карты"):
        assert next(gen)
