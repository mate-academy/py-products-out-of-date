import datetime
from unittest.mock import patch
from app.main import outdated_products


def test_outdated_products_no_expired() -> None:
    today_date = datetime.date(2022, 2, 2)
    products = [
        {"name": "salmon", "expiration_date":
            datetime.date(2022, 2, 10), "price": 600},
        {"name": "chicken", "expiration_date":
            datetime.date(2022, 2, 5), "price": 120},
    ]

    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = today_date
        assert outdated_products(products) == []


def test_outdated_products_some_expired() -> None:
    today_date = datetime.date(2022, 2, 2)
    products = [
        {"name": "salmon", "expiration_date":
            datetime.date(2022, 2, 1), "price": 600},
        {"name": "chicken", "expiration_date":
            datetime.date(2022, 2, 5), "price": 120},
        {"name": "duck", "expiration_date":
            datetime.date(2022, 2, 2), "price": 160},
    ]

    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = today_date
        assert outdated_products(products) == ["salmon"]


def test_outdated_products_all_expired() -> None:
    today_date = datetime.date(2022, 2, 2)
    products = [
        {"name": "salmon", "expiration_date":
            datetime.date(2022, 1, 1), "price": 600},
        {"name": "chicken", "expiration_date":
            datetime.date(2022, 1, 15), "price": 120},
        {"name": "duck", "expiration_date":
            datetime.date(2022, 2, 1), "price": 160},
    ]

    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = today_date
        assert outdated_products(products) == ["salmon", "chicken", "duck"]


def test_outdated_products_empty_list() -> None:
    today_date = datetime.date(2022, 2, 2)
    products = []

    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = today_date
        assert outdated_products(products) == []


def test_outdated_products_today_expired() -> None:
    today_date = datetime.date(2022, 2, 2)
    products = [
        {"name": "salmon", "expiration_date":
            datetime.date(2022, 2, 2), "price": 600},
        {"name": "chicken", "expiration_date":
            datetime.date(2022, 2, 5), "price": 120},
        {"name": "duck", "expiration_date":
            datetime.date(2022, 2, 1), "price": 160},
    ]

    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = today_date
        assert outdated_products(products) == ["duck"]
