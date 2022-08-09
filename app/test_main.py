import datetime
import pytest
from unittest import mock

from app.main import outdated_products


@pytest.fixture()
def products():
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


@pytest.fixture()
def mocked_date():
    with mock.patch("app.main.datetime") as date:
        yield date


def test_of_one_expired_product(products, mocked_date):
    mocked_date.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products) == ["duck"]
