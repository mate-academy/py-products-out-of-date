import datetime
from typing import Any
from unittest import mock
from unittest.mock import Mock

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "expired_products, expected_result", [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 1, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ], [
                "chicken", "duck"
            ]
        )
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(
        mock_datetime: Mock,
        expired_products: list[dict[str, Any]],
        expected_result: list[str]
) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(expired_products) == expected_result
