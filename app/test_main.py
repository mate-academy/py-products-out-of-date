import pytest

import datetime

from unittest import mock

from app.main import outdated_products


@pytest.fixture()
def mocked_datetime():
    with mock.patch("datetime.date") as mocked_datetime_date:
        mocked_datetime_date.return_value = datetime.date(2022, 9, 10)


def test_out_fated_product(mocked_datetime):
    el = ([
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 9, 9),
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
    ])
    assert outdated_products(el) == ['salmon', 'chicken', 'duck']


def test_out_fated2_product(mocked_datetime):
    el = ([
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 9, 11),
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
    ])
    assert outdated_products(el) == ['chicken', 'duck']


def test_out_fated3_product(mocked_datetime):
    el = ([
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 9, 10),
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
    ])
    assert outdated_products(el) == ['salmon', 'chicken', 'duck']
