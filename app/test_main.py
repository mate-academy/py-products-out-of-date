from unittest import mock
import pytest
from app.main import outdated_products
import datetime


@pytest.fixture()
def mocked_date():
    with mock.patch("app.main.datetime") as mocked_date:
        yield mocked_date.date.today


@pytest.fixture()
def products():
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


def test_return_duck_if_due_date_is_feb_2(mocked_date, products):
    mocked_date.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products) == ["duck"]
