import datetime
from unittest.mock import patch

from app.main import outdated_products


class FakeDate(datetime.date):
    @classmethod
    def today(cls) -> "FakeDate":
        return cls(2022, 2, 2)


def test_returns_empty_list_when_no_products_are_outdated() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120,
        },
    ]

    with patch("app.main.datetime.date", FakeDate):
        assert outdated_products(products) == []


def test_returns_only_outdated_products() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120,
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160,
        },
    ]

    with patch("app.main.datetime.date", FakeDate):
        assert outdated_products(products) == ["duck"]


def test_product_expiring_today_is_not_outdated() -> None:
    products = [
        {
            "name": "milk",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 50,
        }
    ]

    with patch("app.main.datetime.date", FakeDate):
        assert outdated_products(products) == []


def test_returns_all_outdated_products_in_original_order() -> None:
    products = [
        {
            "name": "bread",
            "expiration_date": datetime.date(2022, 1, 30),
            "price": 40,
        },
        {
            "name": "cheese",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 90,
        },
        {
            "name": "yogurt",
            "expiration_date": datetime.date(2022, 2, 3),
            "price": 30,
        },
    ]

    with patch("app.main.datetime.date", FakeDate):
        assert outdated_products(products) == ["bread", "cheese"]
