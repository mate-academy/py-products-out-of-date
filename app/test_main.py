import pytest
from unittest import mock
from typing import Any
import datetime
from app.main import outdated_products


@pytest.mark.parametrize("products, expected", [
    ([
        {
            "name": "salmon",
            "expiration_date": datetime.date(2024, 3, 1),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2024, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2024, 3, 2),
            "price": 160
        }
    ], ["salmon", "chicken"])
])
@mock.patch("app.main.datetime")
def test_outdated_products(mock_datetime: Any,
                           products: list[dict],
                           expected: list) -> None:
    mock_datetime.date.today.return_value = datetime.date(2024, 3, 2)
    assert outdated_products(products) == expected

# @mock.patch("app.main.datetime")
# def test_outdated_products(mock_datetime: Any,
#                            products: list[dict],
#                            expected: list) -> None:
#     mock_datetime.date.today.return_value = datetime.date(2024, 3, 2)
#     assert outdated_products(products) == expected
