from app.main import outdated_products

import datetime
from unittest import mock

import pytest


@pytest.fixture
def input_data():
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


@pytest.mark.parametrize(
    "date, result",
    [
        (datetime.date(2022, 2, 1), []),
        (datetime.date(2022, 2, 2), ["duck"]),
        (datetime.date(2022, 2, 6), ["chicken", "duck"]),
        (datetime.date(2022, 2, 13), ["salmon", "chicken", "duck"]),
    ]
)
@mock.patch("datetime.date")
def test_for_outdated_products(mock_date, date, result, input_data):
    mock_date.today.return_value = date
    assert outdated_products(input_data) == result
