from datetime import date
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "products,current_date,expected_result",
    [
        (
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
            date(2022, 2, 2),
            ["duck"]
        ),
        (
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
            date(2022, 2, 10),
            ["chicken", "duck"]
        )
    ]
)
def test_outdated_products(
    products: list,
    current_date: date,
    expected_result: list[str]
) -> None:
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = current_date
        assert outdated_products(products) == expected_result
