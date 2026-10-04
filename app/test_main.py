from datetime import date
from unittest.mock import patch
from app.main import outdated_products
from typing import Any


@patch("app.main.date")
def test_if_not_expired(mock_date: Any) -> None:
    mock_date.today.return_value = date(2022, 2, 3)
    result = outdated_products(
        [
            {
                "name": "salmon",
                "expiration_date": date(2022, 2, 1),
                "price": 600
            }
        ]
    )
    assert result == ["salmon"]


@patch("app.main.date")
def test_if_expired(mock_date: Any) -> None:
    mock_date.today.return_value = date(2022, 1, 3)
    result = outdated_products(
        [
            {
                "name": "salmon",
                "expiration_date": date(2022, 2, 4),
                "price": 600
            }
        ]
    )
    assert result == []


@patch("app.main.date")
def test_if_expired_but_dates_equal(mock_date: Any) -> None:
    mock_date.today.return_value = date(2022, 2, 3)
    result = outdated_products(
        [
            {
                "name": "salmon",
                "expiration_date": date(2022, 2, 3),
                "price": 600
            }
        ]
    )
    assert result == []
