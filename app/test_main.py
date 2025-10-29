import datetime
from unittest import mock
from typing import Any

from app.main import outdated_products


@mock.patch("app.main.datetime.date.today")
def test_outdated_products_two_normal_products(mocked_date: Any) -> None:
    mocked_date.return_value = datetime.date(2025, 10, 28)
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2025, 11, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2025, 12, 10),
            "price": 120
        }
    ]
    assert (
        outdated_products(products) == []
    )


@mock.patch("app.main.datetime.date.today")
def test_outdated_products_two_outdated_products(mocked_date: Any) -> None:
    mocked_date.return_value = datetime.date(2025, 10, 28)
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2025, 12, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2025, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 11),
            "price": 160
        }
    ]
    assert (
        outdated_products(products) == ["chicken", "duck"]
    )
