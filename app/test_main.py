from app.main import outdated_products
from typing import Any
import datetime
import pytest


class NewDate(datetime.date):
    @classmethod
    def today(cls) -> Any:
        return cls(2022, 2, 2)


@pytest.fixture()
def products_pattern() -> list:
    return [
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


def test_different_dates(products_pattern: list[dict]) -> list:
    datetime.date = NewDate
    assert outdated_products(products_pattern) == ["duck"]


def test_all_today_dates(products_pattern: list[dict]) -> list:
    datetime.date = NewDate
    for product in products_pattern:
        product["expiration_date"] = NewDate.today()
    assert outdated_products(products_pattern) == []
