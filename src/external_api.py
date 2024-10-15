import os

import requests
from dotenv import load_dotenv


def convert_into_rubles(transaction: dict) -> float:
    """
    Принимает на вход транзакцию. Возвращает сумму, указанною в транзакции.
    Если сумма транзакции указана не в рублях(а в USD или EUR), конвертирует сумму в рубли.
    Курсы конвертации валют получает обращаясь к стороннему API:
    https://apilayer.com/marketplace/exchangerates_data-api#endpoints
    """
    amount = transaction["operationAmount"]["amount"]
    currency_source_code = transaction["operationAmount"]["currency"]["code"]
    if currency_source_code == "USD" or currency_source_code == "EUR":
        load_dotenv()
        api_key = os.getenv("API_KEY")
        currency_target_code = "RUB"
        url = "https://api.apilayer.com/exchangerates_data/convert"
        payload = {"amount": amount, "from": currency_source_code, "to": currency_target_code}
        headers = {"apikey": api_key}
        response = requests.get(url, headers=headers, params=payload)
        status_code = response.status_code
        result = response.json()
        if status_code != 200:
            raise Exception("Что-то пошло не так!")
        rounded_amount = round(result["result"], 2)
        return float(rounded_amount)
    else:
        return float(amount)
