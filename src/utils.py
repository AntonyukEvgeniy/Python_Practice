import json
from json import JSONDecodeError
from pathlib import Path
from typing import Any


def get_transactions_from_file(filepath: str) -> Any:
    """
    Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    data_folder = Path(__file__).parent.parent
    file_to_open = data_folder / filepath
    try:
        with open(file_to_open, "r", encoding="utf8") as f:
            data = json.load(f)
            print(type(data))
            return data
    except (FileNotFoundError, JSONDecodeError, TypeError, KeyError, ValueError):
        return []
