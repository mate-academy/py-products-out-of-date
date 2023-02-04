import pytest
import datetime
from unittest import mock
from app.main import outdated_products


products = [
    {
        "name": "chicken",
        "expiration_date": datetime.date(2023, 2, 10),
        "price": 90
    },
    {
        "name": "milk",
        "expiration_date": datetime.date(2023, 2, 5),
        "price": 50
    },
    {
        "name": "banana",
        "expiration_date": datetime.date(2023, 2, 1),
        "price": 30
    }
]


@pytest.fixture()
def mocked_datetime_today() -> mock:
    with mock.patch("app.main.datetime", wraps=datetime) as mocked_today:
        yield mocked_today


def test_returns_expired_products(
    mocked_datetime_today: mock
) -> None:
    mocked_datetime_today.date.today.return_value = datetime.date(2023, 2, 10)
    assert outdated_products(products) == ["milk", "banana"]


def test_when_none_expired_returns_no_products(
    mocked_datetime_today: mock
) -> None:
    mocked_datetime_today.date.today.return_value = datetime.date(2023, 2, 1)
    assert outdated_products(products) == []


def test_returns_long_time_expired_products(
    mocked_datetime_today: mock
) -> None:
    mocked_datetime_today.date.today.return_value = datetime.date(2050, 2, 4)
    assert outdated_products(products) == ["chicken", "milk", "banana"]


def test_returns_no_products_with_not_realistic_date(
    mocked_datetime_today: mock
) -> None:
    mocked_datetime_today.date.today.return_value = datetime.date(1984, 2, 4)
    assert outdated_products(products) == []
