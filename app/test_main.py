import pytest
import datetime
from unittest import mock

from app.main import outdated_products

GGG = [
    {
        "name": "salmon",
        "expiration_date": datetime.date(2022, 2, 10),
        "price": 600
    }]


@pytest.mark.parametrize(
    "current_rate, predicted_exchange, result", [
        (GGG, datetime.date(2022, 2, 11), ["salmon"]),
        (GGG, datetime.date(2022, 2, 9), []),
        (GGG, datetime.date(2022, 2, 10), [])

    ]
)
def test_get_exchange_rate_prediction_with_mock(current_rate: list,
                                                predicted_exchange: str,
                                                result: str) -> None:

    with mock.patch("app.main.datetime") as mock_func:
        mock_func.date.today.return_value = predicted_exchange
        assert outdated_products(current_rate) == result
