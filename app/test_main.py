# flake8: noqa: *
import pytest
import datetime
from unittest.mock import patch

from app.main import outdated_products


@pytest.mark.parametrize(
    "expiration_date, expected",
    [
        pytest.param((2026, 1, 20), [], id="Date == Today"),
        pytest.param((2026, 1, 19), ["milk"], id="Date < Today"),
        pytest.param((2026, 1, 21), [], id="Date > Today"),
    ]
)
@patch("app.main.datetime")
def test_outdated_products(mock_datetime, expiration_date, expected):
    mock_datetime.date.today.return_value = datetime.date(2026, 1, 20)

    products = [
        {"name": "milk", "expiration_date": datetime.date(*expiration_date), "price": 50}
    ]

    assert outdated_products(products) == expected

