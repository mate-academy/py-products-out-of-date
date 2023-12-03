import pytest
from unittest.mock import patch
from datetime import date, datetime
from app.main import outdated_products


@pytest.mark.parametrize(
    "mock_date,list_product,expected_result",
    [
        (
            date(2022, 2, 2),
            [
                {
                    "name": "salmon",
                    "expiration_date": date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": date(2022, 2, 1),
                    "price": 160
                }
            ],
            ["duck"]
        ),
        (
                date(2022, 2, 5),
                [
                    {
                        "name": "salmon",
                        "expiration_date": date(2022, 2, 10),
                        "price": 600
                    },
                    {
                        "name": "chicken",
                        "expiration_date": date(2022, 2, 5),
                        "price": 120
                    },
                    {
                        "name": "duck",
                        "expiration_date": date(2022, 2, 1),
                        "price": 160
                    }
                ],
                ["duck"]
        )
    ]
)
def test_outdated_products(mock_date: date, list_product: list, expected_result: list) -> None:
    with patch('datetime.date') as mock_datetime:
        mock_datetime.today.return_value = mock_date
        assert outdated_products(list_product) == expected_result
