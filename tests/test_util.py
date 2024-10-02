from unittest.mock import mock_open, patch

from src.utils import get_transactions_from_file


def test_get_transactions_from_file(filepath):
    result = get_transactions_from_file(filepath)
    assert len(result) > 0


def test_get_transactions_from_file_error():
    result = get_transactions_from_file("/")
    assert len(result) == 0


@patch("builtins.open", new_callable=mock_open, read_data="[]")
def test_get_transactions_from_file_mock(mock_file):
    assert open("path/to/open").read() == "[]"
    mock_file.assert_called_with("path/to/open")
