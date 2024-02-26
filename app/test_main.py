import datetime
from typing import Any
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "product_list, expected_result",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2024, 2, 25),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2024, 2, 26),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2024, 1, 17),
                    "price": 160
                }
            ],
            ["salmon", "duck"]
        )
    ])
@mock.patch("app.main.datetime")
def test_outdated_products(mock_datetime: Any,
                           product_list: list[dict],
                           expected_result: list) -> None:
    mock_datetime.date.today.return_value = datetime.date(2024, 2, 26)
    assert outdated_products(product_list) == expected_result
