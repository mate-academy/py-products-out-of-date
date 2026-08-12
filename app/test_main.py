import datetime
from unittest import mock
from app.main import outdated_products


def test_expired_product() -> list:
    test_outdated = datetime.date(2022, 2, 1)
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
        mock_date.today.return_value = test_outdated
        assert outdated_products(products) == []


def test_empty_list() -> list:
    test_emptty = datetime.date(2022, 2, 5)
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
    with mock.patch("datetime.date") as mock_empty:
        mock_empty.today.return_value = test_emptty
        assert outdated_products(products) == ["duck"]


def test_full_list_of_products() -> list:
    test_full = datetime.date(2022, 2, 11)
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

    with mock.patch("datetime.date") as mock_full:
        mock_full.today.return_value = test_full
        assert outdated_products(products) == ["salmon", "chicken", "duck"]
