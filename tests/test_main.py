import datetime
from unittest import mock
from app.main import outdated_products


@mock.patch("app.main.datetime")
def test_all_products_fresh(mocked_datetime):
    products = [
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
    mocked_datetime.date.today.return_value = \
        datetime.date(2022, 2, 13)
    assert outdated_products(products) == []


@mock.patch("app.main.datetime")
def test_all_products_outdated(mocked_datetime):
    mocked_datetime.date.today.return_value = \
        datetime.date(2022, 12, 9)
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 3),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 1, 4),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2021, 3, 5),
            "price": 160
        }
    ]

    assert outdated_products(products) == ["salmon", "chicken", "duck"]


@mock.patch("app.main.datetime")
def test_not_all_products_outdated(mocked_datetime):
    mocked_datetime.date.today.return_value = \
        datetime.date(2022, 2, 6)
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 3),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 3, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2021, 4, 23),
            "price": 160
        }
    ]
    assert outdated_products(products) == ["salmon", "duck"]
