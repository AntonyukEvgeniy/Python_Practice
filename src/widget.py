import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_pay_info: str) -> str:
    """
    Принимает строку, содержащую тип и номер карты или счета.
    Возвращает строку с замаскированным номером.
    """
    user_info_number = "".join(filter(lambda z: z.isdigit(), user_pay_info))
    user_info_text = "".join(filter(lambda z: z.isalpha(), user_pay_info))
    if user_pay_info.startswith("Счет"):
        bank_account_formated = get_mask_account(user_info_number)
        return f"{user_info_text} {bank_account_formated}"
    card_number_formated = get_mask_card_number(user_info_number)
    return f"{user_info_text} {card_number_formated}"


def get_date(date_to_format: str) -> str:
    """
    Принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате
    "11.03.2024"
    """
    date_formated_datetime = datetime.datetime.strptime(date_to_format, "%Y-%m-%dT%H:%M:%S.%f")
    date_formated_date = date_formated_datetime.strftime("%d.%m.%Y")
    return str(date_formated_date)
