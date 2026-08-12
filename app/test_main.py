import pytest
import datetime

from unittest import mock

from app.main import outdated_products

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


@pytest.fixture()
def mocked_date() -> callable:
    with mock.patch("app.main.datetime") as mocked_day:
        yield mocked_day


def test_all_products(mocked_date: callable) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 11, 11)
    assert outdated_products(products) == ["salmon", "chicken", "duck"]


def test_one_products(mocked_date: callable) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 2, 5)
    assert outdated_products(products) == ["duck"]


def test_zero_products(mocked_date: callable) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 1, 1)
    assert outdated_products(products) == []
