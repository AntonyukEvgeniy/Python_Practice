from typing import Any
from unittest.mock import mock_open, patch

from src.utils_xl import get_transactions_from_csv_file


def test_get_transactions_from_file(filepath_csv: str) -> Any:
    result = get_transactions_from_csv_file(filepath_csv)
    assert len(result) > 0


def test_get_transactions_from_file_error() -> Any:
    result = get_transactions_from_csv_file("/")
    assert len(result) == 0


@patch("builtins.open", new_callable=mock_open, read_data="[]")
def test_get_transactions_from_file_mock(mock_file):
    assert open("path/to/open").read() == "[]"
    mock_file.assert_called_with("path/to/open")
