from unittest.mock import patch
from datetime import date
from app.main import outdated_products


def test_outdated_products() -> None:
    products = [
        {"name": "salmon", "expiration_date": date(2022, 2, 10), "price": 600},
        {"name": "chicken", "expiration_date": date(2022, 2, 5), "price": 120},
        {"name": "duck", "expiration_date": date(2022, 2, 1), "price": 160},
    ]

    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = date(2022, 2, 2)
        assert outdated_products(products) == ["duck"]

    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = date(2022, 2, 5)
        assert outdated_products(products) == ["duck"]

    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = date(2022, 2, 10)
        assert outdated_products(products) == ["chicken", "duck"]

    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = date(2022, 2, 15)
        assert outdated_products(products) == ["salmon", "chicken", "duck"]


def test_outdated_products_empty_list() -> None:
    products = []
    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = date(2022, 2, 2)
        assert outdated_products(products) == []


def test_outdated_products_no_outdated() -> None:
    products = [
        {"name": "salmon", "expiration_date": date(2022, 2, 10), "price": 600},
        {"name": "chicken",
         "expiration_date": date(2022, 2, 15), "price": 120},
        {"name": "duck", "expiration_date": date(2022, 3, 1), "price": 160},
    ]

    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = date(2022, 2, 2)
        assert outdated_products(products) == []
