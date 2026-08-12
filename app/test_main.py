import unittest
from datetime import date
from unittest.mock import patch
from app.main import outdated_products


@patch("datetime.date")
def test_outdated_products(mock_date: unittest.mock.Mock) -> None:
    mock_date.today.return_value = date(2022, 2, 2)
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
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        },
        {
            "name": "milk",
            "expiration_date": date(2022, 2, 2),  # Expires today
            "price": 50
        }
    ]
    result = outdated_products(products)
    assert result == ["duck"]


def product_not_outdated() -> None:
    products_no_outdated = [
        {
            "name": "beef",
            "expiration_date": date(2022, 2, 15),
            "price": 250
        },
        {
            "name": "pork",
            "expiration_date": date(2022, 2, 8),
            "price": 180
        }
    ]

    assert outdated_products(products_no_outdated) == []
