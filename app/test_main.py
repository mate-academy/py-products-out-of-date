from app.main import outdated_products
from unittest import mock
from typing import Any

import pytest


@mock.patch("app.main.datetime")
@pytest.mark.parametrize(
    "product,expected_result",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": 2022210,
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": 202225,
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": 202221,
                    "price": 160
                }
            ],
            ["duck"]
        ),
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": 2022210,
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": 202225,
                    "price": 120
                }
            ],
            []
        ),
    ]
)
def test_outdated_products(
        mocked_datetime: Any,
        product: list,
        expected_result: list
) -> None:
    mocked_datetime.date.today.return_value = 202222
    assert outdated_products(product) == expected_result
