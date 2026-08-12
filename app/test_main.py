import datetime

import pytest
from app.main import outdated_products
from datetime import date
from unittest import mock


@pytest.mark.parametrize(
    "tested_list, expected_list, my_date",
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
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ],
            [
                "duck"
            ],
            date(2022, 2, 2)
        )
    ]
)
@mock.patch("datetime.date")
def tested_outdated_products(
    mocked_tested_date: mock.MagicMock,
    tested_list: list[dict],
    expected_list: list[str],
    my_date: date
) -> None:
    mocked_tested_date.today.return_value = my_date
    assert outdated_products(tested_list) == expected_list
