import datetime
import pytest
from unittest import mock
from app.main import outdated_products


@pytest.fixture()
def products():
    return [{"name": "salmon",
             "expiration_date": datetime.date(2022, 1, 3),
             "price": 650},
            {"name": "chicken",
             "expiration_date": datetime.date(2022, 1, 2),
             "price": 140},
            {"name": "duck",
             "expiration_date": datetime.date(2022, 1, 1),
             "price": 180}]


@mock.patch("app.main.datetime")
def test_all_products_are_fresh(mocked_datetime, products):
    mocked_datetime.date.today.return_value = datetime.date(2020, 1, 4)
    assert outdated_products(products) == []


@mock.patch("app.main.datetime")
def test_all_products_are_outdated(mocked_datetime, products):
    mocked_datetime.date.today.return_value = datetime.date(2022, 1, 4)
    assert outdated_products(products) == ["salmon", "chicken", "duck"]


@mock.patch("app.main.datetime")
def test_expiration_date_of_product(mocked_datetime, products):
    mocked_datetime.date.today.return_value = datetime.date(2022, 1, 2)
    assert outdated_products(products) == ["duck"]
