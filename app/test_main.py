from unittest.mock import patch, Mock

import pytest
import datetime

from app.main import outdated_products


@pytest.fixture()
def products() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2025, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2024, 10, 28),
            "price": 160
        },
        {
            "name": "dog",
            "expiration_date": datetime.date(2024, 10, 27),
            "price": 160
        },
        {
            "name": "cat",
            "expiration_date": datetime.date(2024, 10, 29),
            "price": 160
        }
    ]


@patch("app.main.datetime")
def test_outdated_products(mock_date: Mock, products: list) -> None:
    mock_date.date.today.return_value = datetime.date(2024, 10, 28)
    assert outdated_products(products) == ["salmon", "dog"]
