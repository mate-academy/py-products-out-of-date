import pytest

import datetime

from app.main import outdated_products

from freezegun import freeze_time


@pytest.fixture()
def products_test():
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 11),
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 12),
        }
    ]


@freeze_time("2022-03-01")
def test_all_bad(products_test):
    assert outdated_products(products_test) == ['salmon', 'chicken', 'duck']


@freeze_time("2021-01-01")
def test_all_good(products_test):
    assert outdated_products(products_test) == []


@freeze_time("2022-02-12")
def test_expiration_day_yesterday_outdated(products_test):
    assert outdated_products(products_test) == ['salmon', 'chicken']
