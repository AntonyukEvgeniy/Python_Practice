from typing import Union


def filter_by_state(*, transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Принимает список словарей и опционально значение для ключа state.
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ равен state.
    """
    filtred_transactions = [transaction for transaction in transactions if transaction["state"] == state]
    return filtred_transactions


def sort_by_date(*, transactions: list[dict], sort_order: bool = True) -> list[dict]:
    """
    Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате.
    """
    return sorted(transactions, key=lambda transaction: transaction["date"], reverse=sort_order)
