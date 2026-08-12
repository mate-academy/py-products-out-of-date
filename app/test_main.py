import pytest
from unittest import mock
import datetime
from app.main import outdated_products


@pytest.fixture()
def list_of_products():
    products = [
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
    yield products


@mock.patch("app.main.datetime")
def test_out_of_date(mocked_datetime_date, list_of_products):
    mocked_datetime_date.date.today.return_value = datetime.date(2022, 2, 3)
    assert outdated_products(list_of_products) == ["duck"]
