import unittest.mock
from typing import Callable

import pytest
from app.main import outdated_products


@pytest.mark.parametrize(
    "products_list, expected",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": "2022-02-13",
                    "price": 600
                },
                {
                    "name": "sanjak",
                    "expiration_date": "2022-02-10",
                    "price": 600
                }
            ],
            ["sanjak"],
        ),

        (
            [
                {
                    "name": "salmon",
                    "expiration_date": "2022-02-11",
                    "price": 600
                },
            ],
            []
        )
    ]
)
@unittest.mock.patch("app.main.datetime.date")
def test_outdated_products(mock_date: Callable,
                           products_list: list, expected: list) -> None:
    mock_date.today.return_value = "2022-02-11"
    assert outdated_products(products_list) == expected
