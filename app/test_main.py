from unittest import mock
from datetime import date

import pytest

from app.main import outdated_products


@pytest.fixture()
def mocked_date():
    with mock.patch("datetime.date") as mock_date:
        yield mock_date


@pytest.fixture()
def product_list():
    return [
        {
            "name": "salmon",
            "expiration_date": date(2022, 12, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 10, 5),
            "price": 120
        }
    ]


def test_should_return_correct_expired_products(product_list, mocked_date):
    mocked_date.today.return_value = date(2022, 10, 6)
    assert outdated_products(product_list) == ["chicken"]


def test_should_return_empty_list_if_all_products_are_ok(product_list,
                                                         mocked_date):
    mocked_date.today.return_value = date(2022, 10, 4)
    assert outdated_products(product_list) == []


def test_should_not_return_product_if_exp_date_eq_today(product_list,
                                                        mocked_date):
    mocked_date.today.return_value = date(2022, 10, 5)
    assert outdated_products(product_list) == []
