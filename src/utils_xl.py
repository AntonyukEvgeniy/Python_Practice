import csv
import logging
from pathlib import Path
from typing import Any

import pandas as pd


def file(filepath: str) -> Path:
    data_folder = Path(__file__).parent.parent
    file_to_open = data_folder / filepath
    return file_to_open


logger = logging.getLogger(__name__)
logs_file = file("logs/utils_xl.log")
file_handler = logging.FileHandler(logs_file, mode="w")
logger.addHandler(file_handler)
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.setLevel(logging.DEBUG)


def get_transactions_from_csv_file(filepath: str) -> Any:
    """
    Принимает на вход путь до csv-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    file_to_open = file(filepath)
    try:
        transactions_from_scv = []
        with open(file_to_open, encoding="utf8") as f:
            reader = csv.DictReader(f, delimiter=";")
            for row in reader:
                transactions_from_scv.append(row)
        logger.debug(f"Файл {file_to_open} успешно прочитан")
        return transactions_from_scv
    except Exception as e:
        logging.error(e)
        return []


def get_transactions_from_xlsx_file(filepath: str) -> Any:
    """
    Принимает на вход путь до exel-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        file_to_open = file(filepath)
        excel_data = pd.read_excel(file_to_open)
        excel_data.fillna("", inplace=True)
        logger.debug(f"Файл {file_to_open} успешно прочитан")
        return excel_data.to_dict("records")
    except Exception as e:
        logging.error(e)
        return []
