import pytest
from unittest.mock import patch
import datetime
from typing import Any
import app.main


@pytest.mark.parametrize(
    "date, current_inventory, result",
    [
        (datetime.date(2025, 11, 29), [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2025, 11, 30),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2025, 11, 29),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2025, 11, 28),
                "price": 160
            }
        ], ["duck"])]
)
@patch("app.main.datetime.date")
def test_outdated_products(mock_date: Any,
                           date: Any,
                           current_inventory: list[dict],
                           result: list) -> None:
    mock_date.today.return_value = date
    test_result = app.main.outdated_products(current_inventory)
    assert test_result == result
