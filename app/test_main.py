from unittest.mock import MagicMock
from unittest import mock
from datetime import date

from app.main import outdated_products

import pytest


@pytest.fixture
def products() -> list:
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
            "expiration_date": date(2022, 2, 2),
            "price": 160
        }
    ]


@pytest.mark.parametrize(
    "today_date,expected",
    [
        (date(2022, 2, 1), []),
        (date(2022, 2, 2), []),
        (date(2022, 2, 10), ["chicken", "duck"]),
        (date(2022, 2, 11), ["salmon", "chicken", "duck"])
    ],
    ids=[
        "should return empty list",
        "should not include an item "
        "if expiration date is same as today's date",
        "should return list with two items",
        "should return list with three items"
    ]
)
@mock.patch("datetime.date")
def test_outdated_products(
        mock_date: MagicMock,
        today_date: date,
        expected: list,
        products: list
) -> None:
    mock_date.today.return_value = today_date
    assert outdated_products(products) == expected
