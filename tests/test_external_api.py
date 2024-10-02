from unittest.mock import patch

from src.external_api import convert_into_rubles

transaction = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560",
}
convert_service_returned_value = {
    "success": True,
    "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
    "info": {"timestamp": 1727880019, "rate": 95.023275},
    "date": "2024-10-02",
    "result": 777777.77,
}


@patch("requests.get")
def test_convert_into_rubles(mock_get):
    mock_get.return_value.json.return_value = convert_service_returned_value
    mock_get.return_value.status_code = 200
    assert convert_into_rubles(transaction) == 777777.77
    mock_get.assert_called()
