from unittest import mock
from datetime import date
from typing import Any

from app.main import outdated_products


@mock.patch("datetime.date")
def test_outdated_products(today: Any) -> None:
    mock.MagicMock.return_value = date(2022, 2, 2)
    products = [
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        }
    ]
    assert outdated_products(products) == ["duck"]


@mock.patch("datetime.date")
def test_not_expired(today: Any) -> None:
    mock.MagicMock.return_value = date(2022, 2, 5)
    products = [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 5),
            "price": 120
        }
    ]
    assert outdated_products(products) == []
