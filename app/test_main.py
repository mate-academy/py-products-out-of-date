from datetime import date
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.fixture()
def mocked_datetime():
    with mock.patch("app.main.datetime") as mocked_time:
        yield mocked_time


@pytest.fixture()
def products():
    return [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        }
    ]


@pytest.mark.parametrize(
    "date_to_check,expected_result", [
        (date(2022, 2, 9), ["chicken", "duck"]),
        (date(2022, 1, 26), []),
        (date(2022, 2, 4), ["duck"]),
        (date(2022, 2, 13), ["salmon", "chicken", "duck"]),
        (date.today(), ["salmon", "chicken", "duck"])
    ]
)
def test_outdated_products_for_correct_values(mocked_datetime,
                                              products,
                                              date_to_check,
                                              expected_result):
    mocked_datetime.date.today.return_value = date_to_check
    assert outdated_products(products) == expected_result
