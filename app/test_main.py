from app.main import outdated_products
from unittest import mock
import datetime


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


def test_date_less_today() -> None:

    class MockDate(datetime.date):
        @classmethod
        def today(cls) -> object:
            return cls(2022, 2, 2)

    with mock.patch("app.main.datetime.date", MockDate):
        assert outdated_products(products) == ["duck"]


def test_date_equal_today() -> None:

    class MockDate(datetime.date):
        @classmethod
        def today(cls) -> object:
            return cls(2022, 2, 1)

    with mock.patch("app.main.datetime.date", MockDate):
        assert outdated_products(products) == []


def test_date_more_today() -> None:

    class MockDate(datetime.date):
        @classmethod
        def today(cls) -> object:
            return cls(2022, 2, 11)

    with mock.patch("app.main.datetime.date", MockDate):
        assert outdated_products(products) == ["salmon", "chicken", "duck"]
