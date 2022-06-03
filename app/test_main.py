import datetime
import pytest

from unittest import mock

from app.main import outdated_products


@pytest.fixture()
def products():
    yield [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 6, 2),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 5, 1),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2021, 5, 31),
            "price": 160
        }
    ]


@mock.patch("app.main.datetime")
def test_all_products_are_fresh(mocked_datetime, products):

    mocked_datetime.date.today.return_value = datetime.date(2022, 6, 3)

    assert outdated_products(products) == ["salmon", "chicken", "duck"]


@mock.patch("app.main.datetime")
def test_all_products_are_outdated(mocked_datetime, products):

    mocked_datetime.date.today.return_value = datetime.date(2020, 6, 3)

    assert outdated_products(products) == []


@mock.patch("app.main.datetime")
def test_some_products_are_outdated(mocked_datetime, products):

    mocked_datetime.date.today.return_value = datetime.date(2021, 6, 3)

    assert outdated_products(products) == ["duck"]
