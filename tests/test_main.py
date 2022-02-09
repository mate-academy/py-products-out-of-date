import pytest
import datetime
from random import choice
from unittest import mock
from app.main import outdated_products


@pytest.fixture()
def products():
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 13),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 14),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 15),
            "price": 160
        }
    ]


@mock.patch("app.main.datetime")
def test_all_products_fresh(mocked_datetime, products):
    mocked_datetime.date.today.return_value = \
        datetime.date(2022, 2, 13)
    assert outdated_products(products) == []


@mock.patch("app.main.datetime")
def test_all_products_outdated(mocked_datetime, products):
    mocked_datetime.date.today.return_value = \
        datetime.date(2021, 12, 9)
    for product in products:
        product["expiration_date"] = \
            datetime.date(2021, 12, choice((1, 5, 6, 2)))
    assert outdated_products(products) == ["salmon", "chicken", "duck"]


@mock.patch("app.main.datetime")
def test_not_all_products_outdated(mocked_datetime, products):
    mocked_datetime.date.today.return_value = \
        datetime.date(2022, 2, 6)
    for product in products:
        product["expiration_date"] = \
            datetime.date(2022, 2, products.index(product) + 4)
    assert outdated_products(products) == ["salmon", "chicken"]
