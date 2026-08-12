import datetime
from typing import List

import pytest
from unittest.mock import patch

from app.main import outdated_products


@pytest.mark.parametrize(
    "today, products, expected_outdated",
    [
        (
            datetime.date(2025, 8, 29),
            [
                {
                    "name": "лосось",
                    "expiration_date": datetime.date(2025, 8, 29)
                },
                {
                    "name": "курка",
                    "expiration_date": datetime.date(2025, 9, 10)
                }
            ],
            [],
        ),
        (
            datetime.date(2025, 8, 18),
            [
                {
                    "name": "качка",
                    "expiration_date": datetime.date(2025, 8, 10)
                },
                {
                    "name": "курка",
                    "expiration_date": datetime.date(2025, 8, 5)
                },
                {
                    "name": "яблуко",
                    "expiration_date": datetime.date(2025, 9, 10)
                }
            ],
            ["качка", "курка"],
        ),
        (
            datetime.date(2025, 8, 20),
            [
                {
                    "name": "груша",
                    "expiration_date": datetime.date(2025, 9, 20)
                },
                {
                    "name": "слива",
                    "expiration_date": datetime.date(2025, 8, 21)
                },
            ],
            [],
        ),
        (
            datetime.date(2025, 8, 18),
            [

            ],
            [],
        ),
        (
            datetime.date(2025, 8, 18),
            [
                {
                    "name": "груша",
                    "expiration_date": datetime.date(2025, 9, 20)
                },
                {
                    "name": "слива",
                    "expiration_date": datetime.date(2025, 8, 17)
                },
            ],
            ["слива"]
        )

    ]
)
@patch("app.main.datetime.date")
def test_outdated_products(
        mock_date: datetime,
        today: datetime,
        products: List[dict],
        expected_outdated: datetime
) -> None:
    mock_date.today.return_value = today
    result = outdated_products(products)
    assert result == expected_outdated
