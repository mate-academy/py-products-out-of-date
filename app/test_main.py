from app.main import outdated_products
import pytest
from unittest import mock
import datetime


@pytest.fixture()
def test_outdated_products():
    result = [
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
    return result


@mock.patch("app.main.datetime")
def test_date(mocked_data, test_outdated_products):
    mocked_data.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(test_outdated_products) == ["duck"]
