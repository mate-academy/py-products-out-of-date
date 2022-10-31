import pytest

from app.main import outdated_products

import datetime

from unittest import mock


@pytest.fixture()
def mocked_datetime():
    with mock.patch("app.main.datetime") as date:
        yield date


@pytest.fixture()
def dict_product():
    return [
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


def test_outdated_products(dict_product, mocked_datetime):
    mocked_datetime.date.today.return_value = datetime.date(2022, 2, 3)
    assert outdated_products(dict_product) == ["duck"]
