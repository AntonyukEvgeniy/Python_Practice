import json
import logging
from json import JSONDecodeError
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/utils.log", mode="w")
logger.addHandler(file_handler)
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.setLevel(logging.DEBUG)


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
            logger.debug("Файл успешно распарсен.")
            return data
    except (FileNotFoundError, JSONDecodeError, TypeError, KeyError, ValueError):
        logger.error("Произошла ошибка при попытке распарсить файл. Результат: []")
        return []
