import datetime
import pytest
from app.main import outdated_products
from unittest import mock


@pytest.mark.parametrize(
    "today_date, product, expected", [
        (datetime.date(2022, 2, 2), [
            {"name": "salmon", "expiration_date": datetime.date(2022, 2, 10), "price": 600},
            {"name": "chicken", "expiration_date": datetime.date(2022, 2, 5), "price": 120},
            {"name": "duck", "expiration_date": datetime.date(2022, 2, 1), "price": 160}
        ], ["duck"]),

        (datetime.date(2022, 3, 1),[
            {"name": "milk", "expiration_date": datetime.date(2022, 2, 28), "price": 50},
            {"name": "bread", "expiration_date": datetime.date(2022, 3, 2), "price": 20}
        ], ["bread"]),

        (datetime.date(2022, 1, 1), [
            {"name": "apple", "expiration_date": datetime.date(2022, 1, 10), "price": 5},
            {"name": "banana", "expiration_date": datetime.date(2022, 1, 1), "price": 3}
        ], []),

        (datetime.date(2022, 12, 31), [], []),
])
def test_outdated_products(today_date, product, expected):
    with mock.patch("datetime.date.today", return_value=today_date):
        assert outdated_products(product) == expected
