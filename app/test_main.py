from unittest.mock import patch
import datetime
from app.main import outdated_products


def test_outdated_products_no_outdated() -> None:
    with patch("datetime.date.today") as mock_today:
        mock_today.return_value = datetime.date(2022, 2, 2)

        products = [
            {"name": "salmon", "expiration_date": datetime.date(2022, 2, 10),
             "price": 600},
            {"name": "chicken", "expiration_date": datetime.date(2022, 2, 5),
             "price": 120},
            {"name": "duck", "expiration_date": datetime.date(2022, 2, 1),
             "price": 160},
        ]
        assert outdated_products(products) == []


def test_outdated_products_some_outdated() -> None:
    with patch("datetime.date.today") as mock_today:
        mock_today.return_value = datetime.date(2022, 2, 6)

        products = [
            {"name": "salmon", "expiration_date": datetime.date(2022, 2, 10),
             "price": 600},
            {"name": "chicken", "expiration_date": datetime.date(2022, 2, 5),
             "price": 120},
            {"name": "duck", "expiration_date": datetime.date(2022, 2, 1),
             "price": 160},
        ]
        assert outdated_products(products) == ["chicken", "duck"]


def test_outdated_products_all_outdated() -> None:
    with patch("datetime.date.today") as mock_today:
        mock_today.return_value = datetime.date(2022, 2, 11)

        products = [
            {"name": "salmon", "expiration_date": datetime.date(2022, 2, 10),
             "price": 600},
            {"name": "chicken", "expiration_date": datetime.date(2022, 2, 5),
             "price": 120},
            {"name": "duck", "expiration_date": datetime.date(2022, 2, 1),
             "price": 160},
        ]
        assert outdated_products(products) == ["salmon", "chicken", "duck"]
