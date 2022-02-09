from app.main import outdated_products
from unittest import mock
import datetime


@mock.patch("app.main.datetime")
def test_when_all_products_is_expired(mocked_date):
    mocked_date.date.today = mock.Mock(return_value=datetime.date(2022, 2, 15))

    assert outdated_products([
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 14),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2000, 12, 31),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2021, 2, 18),
            "price": 160
        }
    ]) == ['salmon', 'chicken', 'duck']


@mock.patch("app.main.datetime")
def test_when_some_products_is_expired(mocked_date):
    mocked_date.date.today = mock.Mock(return_value=datetime.date(2022, 2, 20))

    assert outdated_products([
        {
            "name": "pork",
            "expiration_date": datetime.date(2025, 1, 14),
            "price": 600
        },
        {
            "name": "fish",
            "expiration_date": datetime.date(2022, 1, 25),
            "price": 120
        },
        {
            "name": "soda",
            "expiration_date": datetime.date(2022, 12, 1),
            "price": 160
        }
    ]) == ['fish']


@mock.patch("app.main.datetime")
def test_when_all_products_not_expired(mocked_date):
    mocked_date.date.today = mock.Mock(return_value=datetime.date(2014, 2, 20))

    assert outdated_products([
        {
            "name": "pork",
            "expiration_date": datetime.date(2025, 1, 14),
            "price": 600
        },
        {
            "name": "fish",
            "expiration_date": datetime.date(2022, 1, 25),
            "price": 120
        },
        {
            "name": "soda",
            "expiration_date": datetime.date(2022, 12, 1),
            "price": 160
        }
    ]) == []
