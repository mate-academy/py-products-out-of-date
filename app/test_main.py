import pytest
import datetime
from unittest import mock

from app.main import outdated_products


@pytest.fixture()
def list_of_products():
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


@mock.patch("app.main.datetime")
def test_outdated_products(mock_datetime, list_of_products):
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(list_of_products) == ['duck']
