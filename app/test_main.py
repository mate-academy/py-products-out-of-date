import datetime
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.fixture()
def product():
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 8, 13),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 8, 12),
            "price": 120
        }
    ]


@mock.patch("app.main.datetime")
def test_no_fresh(mock_date_today, product):
    mock_date_today.date.today.return_value = datetime.date(2022, 8, 13)
    assert outdated_products(product) == ["chicken"]
