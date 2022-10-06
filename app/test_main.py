import pytest
from unittest import mock
from datetime import date
from app.main import outdated_products

incoming_products = [
    {
        "name": "salmon",
        "expiration_date": date(2022, 2, 10),
        "price": 600
    },
    {
        "name": "chicken",
        "expiration_date": date(2022, 2, 5),
        "price": 120
    },
    {
        "name": "duck",
        "expiration_date": date(2022, 2, 1),
        "price": 160
    }
]


@pytest.fixture()
def mocked_today():
    with mock.patch("app.main.datetime") as mock_today:
        yield mock_today


def test_none_outdated_products(mocked_today):
    mocked_today.date.today.return_value = date(2022, 2, 1)
    assert outdated_products(incoming_products) == []


def test_one_outdated_products(mocked_today):
    mocked_today.date.today.return_value = date(2022, 2, 5)
    assert outdated_products(incoming_products) == ["duck"]


def test_all_outdated_products(mocked_today):
    mocked_today.date.today.return_value = date(2022, 2, 11)
    assert outdated_products(incoming_products) == [
        "salmon",
        "chicken",
        "duck"
    ]
