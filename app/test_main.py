import pytest
import datetime
from app.main import outdated_products
from unittest import mock


class FakeDate(datetime.date):
    @classmethod
    def today(cls) -> datetime.date:
        return cls(2025, 12, 3)


@pytest.fixture
def list_products() -> list:
    return [
        {"name": "salmon",
         "expiration_date": datetime.date(2025, 11, 26),
         "price": 104},
        {"name": "chicken",
         "expiration_date": datetime.date(2025, 12, 4),
         "price": 456},
        {"name": "duck",
         "expiration_date": datetime.date(2025, 12, 3),
         "price": 462},
        {"name": "fat",
         "expiration_date": datetime.date(2026, 12, 5),
         "price": 166},
        {"name": "honey",
         "expiration_date": datetime.date(2100, 12, 21),
         "price": 666},
        {"name": "stew",
         "expiration_date": datetime.date(2034, 10, 10),
         "price": 777},
    ]


def test_list_products(list_products: list) -> None:
    with mock.patch("app.main.datetime.date", FakeDate):
        assert outdated_products(list_products) == ["salmon", "chicken"]
