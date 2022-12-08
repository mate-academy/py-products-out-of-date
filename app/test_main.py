from .main import outdated_products
from typing import Callable
from unittest import mock
import datetime
import pytest


@pytest.fixture()
def products() -> list:
    products_list = \
        [
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
    return products_list


@pytest.fixture()
def mocked_date() -> None:
    with mock.patch("app.main.datetime") as mocked_day:
        yield mocked_day


def test_one_outdated_product(mocked_date: mock,
                              products: Callable) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products) == ["duck"]


def test_two_outdated_products(mocked_date: mock,
                               products: Callable) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 2, 7)
    assert outdated_products(products) == ["chicken", "duck"]


def test_three_outdated_products(mocked_date: mock,
                                 products: Callable) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 2, 11)
    assert outdated_products(products) == ["salmon", "chicken", "duck"]


def test_no_outdated_product(mocked_date: mock,
                             products: Callable) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 1, 31)
    assert outdated_products(products) == []
