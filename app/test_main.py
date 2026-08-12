from unittest import mock
from datetime import date

import pytest
import datetime

from app.main import outdated_products


@pytest.mark.parametrize(
    "expiration_date_list, result, datatime_real",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2024, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2024, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2024, 2, 1),
                    "price": 160
                },
            ],
            ["duck"],
            date(2024, 2, 2)
        ),
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2024, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2024, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2024, 2, 1),
                    "price": 160
                }
            ],
            ["chicken", "duck"],
            date(2024, 2, 6)
        ),
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2024, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2024, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2024, 2, 1),
                    "price": 160
                }
            ],
            ["chicken", "duck"],
            date(2024, 2, 10)
        )
    ]
)
@mock.patch("datetime.date")
def test_return_name(
        mock_date: mock,
        expiration_date_list: list[dict],
        result: list[str],
        datatime_real: datetime) -> None:
    mock_date.today.return_value = datatime_real
    assert outdated_products(expiration_date_list) == result
