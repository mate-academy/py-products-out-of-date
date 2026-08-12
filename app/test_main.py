from app.main import outdated_products
import pytest
from unittest import mock
import datetime


@pytest.fixture()
def test_date_out():
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
    return products


@mock.patch("app.main.datetime")
def test_outdate_product(mocked_time, test_date_out):
    mocked_time.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products=test_date_out) == ['duck']
