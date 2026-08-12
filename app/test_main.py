import datetime
from typing import Any, Dict, List
from unittest.mock import patch

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "today_date, products, expected_result",
    [
        (
            datetime.date(2022, 2, 2),
            [
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
                },
            ],
            ["duck"],
        ),
        (
            datetime.date(2022, 2, 1),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 600
                },
            ],
            [],
        ),
        (
            datetime.date(2023, 1, 1),
            [
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
            ],
            ["salmon", "chicken"],
        ),
        (datetime.date(2022, 2, 2), [], []),
    ],
)
@patch("app.main.datetime.date")
def test_outdated_products(
    mock_date: Any,
    today_date: datetime.date,
    products: List[Dict[str, Any]],
    expected_result: List[str],
) -> None:
    """
    Tests the outdated_products function with various scenarios.
    """
    mock_date.today.return_value = today_date
    assert outdated_products(products) == expected_result
