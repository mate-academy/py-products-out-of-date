from unittest import mock
import pytest
import datetime
from app.main import outdated_products


@pytest.fixture()
def mocked_date():
    with mock.patch("app.main.datetime") as mock_date:
        yield mock_date


@pytest.fixture()
def products_template():
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


def test_one_good(mocked_date, products_template):
    mocked_date.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products_template) == ["duck"]
