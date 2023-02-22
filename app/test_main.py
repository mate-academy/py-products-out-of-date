from unittest import mock
import datetime
import pytest

from app.main import outdated_products


@pytest.fixture()
def products_with_dates() -> None:
    return [{
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
        "expiration_date": datetime.date(2022, 2, 4),
        "price": 160
    }]


class Today(datetime.date):
    @classmethod
    def today(cls) -> object:
        return cls(2022, 2, 6)


class Yesterday(datetime.date):
    @classmethod
    def today(cls) -> object:
        return cls(2022, 2, 5)


@mock.patch("app.main.datetime.date", Yesterday)
def test_last_day_yesterday(products_with_dates: list) -> None:
    assert outdated_products(products_with_dates) == ["duck"]


@mock.patch("app.main.datetime.date", Today)
def test_last_day_today(products_with_dates: list) -> None:
    assert outdated_products(products_with_dates) == ["chicken", "duck"]
