# write your code here
import pytest
from typing import Callable
from datetime import date
from unittest.mock import patch
from app.main import outdated_products


@pytest.mark.parametrize(
    "day_of_month, expected_result",
    [
        (date(2022, 1, 29), []),
        (date(2022, 2, 11), ["alex", "smith", "duck"]),
        (date(2022, 2, 1), []),
        (date(2022, 2, 2), ["duck"]),
        (date(2022, 2, 9), ["smith", "duck"]),
    ]
)
@patch("datetime.date")
def test_outdated_products(
        mocked_date: Callable,
        day_of_month: date,
        expected_result: list
) -> None:
    mocked_date.today.return_value = day_of_month
    products = [
        {
            "name": "alex",
            "expiration_date": date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "smith",
            "expiration_date": date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        }
    ]
    assert outdated_products(products) == expected_result
