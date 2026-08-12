import datetime
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "all_products,today,bad_products",
    [
        (
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
                }
            ],
            datetime.date(2022, 2, 2),
            ["duck"]

        ),
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2025, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2025, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2024, 2, 1),
                    "price": 160
                }
            ],
            datetime.date(2023, 2, 2),
            []

        ),
        (
            [
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 3, 1),
                    "price": 160
                }
            ],
            datetime.date(2022, 3, 1),
            []

        )
    ]
)
@mock.patch("datetime.date")
def test_outdated_products(
        mocked_date: mock.MagicMock,
        all_products: dict[list],
        today: datetime.date,
        bad_products: dict[list]) -> None:
    mocked_date.today.return_value = today
    assert outdated_products(all_products) == bad_products
    print(type(today))
