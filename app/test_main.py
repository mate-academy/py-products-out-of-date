from unittest import mock
from app.main import outdated_products
import datetime


def test_outdated_products_before_expiration_date() -> None:
    test_date = datetime.date(2022, 2, 5)
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]

    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = test_date
        assert outdated_products(products) == ["duck"]


def test_should_return_empty() -> None:
    test_date = datetime.date(2022, 2, 1)
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]

    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = test_date
        assert outdated_products(products) == []


def test_should_return_all_products_which_yesterday_outdated() -> None:
    test_date = datetime.date(2022, 2, 11)
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = test_date
        assert outdated_products(products) == ["salmon", "chicken", "duck"]
