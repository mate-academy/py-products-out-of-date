import datetime

import pytest

from unittest import mock

from app.main import outdated_products


def test_return_empty_list_when_input_empty_list():
    assert outdated_products([]) == []


@pytest.fixture
def products_template():
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 7, 30),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 7, 29),
            "price": 160
        }
    ]


@mock.patch("app.main.datetime")
def test_return_outdated_products(mocked_today, products_template):
    mocked_today.date.today.return_value = datetime.date(2022, 7, 30)
    assert outdated_products(products_template) == ["duck"]
