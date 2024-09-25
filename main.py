from src.masks import get_mask_card_number, get_mask_account


transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "55555.55", "currency": {"name": "RU", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "Euro", "code": "EUR"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
]


# for tran in transactions:
#     print(tran["operationAmount"]["currency"]["code"])
# usd_transactions = filter_by_currency(transactions, "USD")
# for _ in range(2):
#     print(next(usd_transactions))
# #
# descriptions = transaction_descriptions(transactions)
# for _ in range(4):
#     print(next(descriptions))
# for card_number in card_number_generator(1, 5):
#     print(card_number)


# get_mask_account(73654108430135874305)
# get_mask_account("73654108430135874305_777")
# mask_account_card("Visa Platinum 7000792289606361")

get_mask_account(73654108430135874305)
get_mask_card_number(2202208131326309)
print(get_mask_card_number(2202208131326309))
