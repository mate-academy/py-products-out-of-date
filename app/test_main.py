from datetime import date
from unittest import mock
import pytest
import datetime

from app.main import outdated_products


@pytest.mark.parametrize(
    "product, result, today_date",
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
            ["duck"],
            date(2022, 2, 2)
        ),
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
            ["chicken", "duck"],
            date(2022, 2, 6)
        ),
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
            ["chicken", "duck"],
            date(2022, 2, 10)
        ),
    ]
)
@mock.patch("datetime.date")
def test_outdated_products(mock_date: mock,
                           product: list[dict],
                           result: list[str],
                           today_date: datetime.date) -> None:
    mock_date.today.return_value = today_date
    assert (outdated_products(product) == result)
