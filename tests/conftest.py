from typing import Union

import pytest


@pytest.fixture
def card_number() -> str:
    return "2202208131326309"


@pytest.fixture
def bank_account_number() -> str:
    return "828912781271872AAA"

@pytest.fixture
def user_pay_info() -> str:
    return "Visa Gold 5999414228426353"