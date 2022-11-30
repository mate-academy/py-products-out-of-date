import datetime

import pytest

from app.main import outdated_products

from unittest import mock


@pytest.fixture(scope="function")
def products_list() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 11, 29),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 11, 29),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 11, 29),
            "price": 160
        }
    ]
    yield products


@pytest.fixture(scope="function")
def another_products_list() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 11, 30),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 11, 30),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 11, 30),
            "price": 160
        }
    ]
    yield products


@pytest.fixture()
def mocked_datatime() -> None:
    with mock.patch("datetime.date.today") as mock_test_datatime:
        yield mock_test_datatime


def test_function_return_len(products_list: list) -> None:
    assert outdated_products(products_list) == ["salmon", "chicken", "duck"]


def test_should_return_empty_list(another_products_list: list) -> None:
    assert outdated_products(another_products_list) == []


def test_should_raise_error_if_func_return_is_str(products_list: list) -> None:
    with pytest.raises(TypeError):
        outdated_products("cheese")
