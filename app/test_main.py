import datetime
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.fixture()
def product_list():
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 9, 30),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 9, 22),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 9, 20),
            "price": 160
        }
    ]
    yield products


@mock.patch("app.main.datetime")
def test_product_out_of_date(mocked_datetime_date, product_list):
    mocked_datetime_date.date.today.return_value = datetime.date(2022, 9, 23)
    assert outdated_products(product_list) == ["duck", "chicken"]
