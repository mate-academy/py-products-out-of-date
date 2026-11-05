import datetime
from unittest.mock import patch
import pytest
from typing import Any

from app.main import outdated_products


@pytest.mark.parametrize(
    "today_date, products, expected",
    [
        (
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600,
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120,
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160,
                },
            ],
            ["duck"],
        ),
        (
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "expired_yesterday",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 100,
                },
                {
                    "name": "expires_today",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 100,
                },
                {
                    "name": "expires_tomorrow",
                    "expiration_date": datetime.date(2022, 2, 3),
                    "price": 100,
                },
            ],
            ["expired_yesterday"],
        ),
        (
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "fresh_milk",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 50,
                },
            ],
            [],
        ),
        (
            datetime.date(2022, 2, 2),
            [],
            [],
        ),
    ],
)
@patch("app.main.datetime.date")
def test_outdated_products(
    mock_date: Any,
    today_date: datetime.date,
    products: list[dict],
    expected: list[str],
) -> None:
    mock_date.today.return_value = today_date

    result = outdated_products(products)

    assert result == expected
