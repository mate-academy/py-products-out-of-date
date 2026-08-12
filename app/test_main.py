from app.main import outdated_products
from unittest.mock import patch
import datetime
import pytest


@pytest.mark.parametrize(
    "today_date,products,expected_outdated",
    [
        (
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ],
            ["duck"]
        ),

        (
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 120
                }
            ],
            []
        ),

        (
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 3),
                    "price": 600
                }
            ],
            []
        ),

        (
            datetime.date(2022, 2, 2),
            [],
            []
        ),

        (
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 3),
                    "price": 600
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 120
                }
            ],
            ["duck"]
        )
    ]
)
def test_outdated_products(
        today_date: str,
        products: list,
        expected_outdated: str
) -> None:
    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = today_date
        result = outdated_products(products)
        assert result == expected_outdated
