from datetime import date

from unittest import mock

import pytest

from app.main import outdated_products


@pytest.fixture()
def mocked_datetime():
    with mock.patch("datetime.date") as mocked:
        yield mocked


@pytest.fixture()
def products():
    return [
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


def test_outdated_products(products, mocked_datetime):
    mocked_datetime.today.return_value = date(2022, 2, 5)
    assert outdated_products(products) == ["duck"]


def test_outdated_products_zero(products, mocked_datetime):
    mocked_datetime.today.return_value = date(2022, 2, 6)
    assert outdated_products(products) == ["chicken", "duck"]
