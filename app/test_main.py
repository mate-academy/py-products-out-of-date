from unittest.mock import patch
from app.main import outdated_products
from datetime import date


@patch("app.main.datetime.date")
def test_outdated_products_today(mock_date: object) -> None:
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
        }
    ]

    assert outdated_products(products) == ["duck"]


@patch("app.main.datetime.date")
def test_outdated_products_yesterday(mock_date: object) -> None:
    mock_date.today.return_value = date(2022, 2, 1)

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
        }
    ]

    assert outdated_products(products) == ["salmon", "chicken", "duck"]


@patch("app.main.datetime.date")
def test_outdated_products(mock_date: object) -> None:
    mock_date.today.return_value = date(2022, 2, 11)

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
        }
    ]

    assert outdated_products(products) == ["salmon", "chicken", "duck"]
