import datetime

import pytest
from unittest import mock

from app.main import outdated_products


@mock.patch("app.main.datetime")
@pytest.mark.parametrize(
    "product, expected_list",
    [
        ([
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 10),
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2024, 10, 21),
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2023, 10, 30),
            },
            {
                "name": "cheese",
                "expiration_date": datetime.date(2023, 10, 28),
            },
            {
                "name": "fish",
                "expiration_date": datetime.date(2023, 10, 29),
            },
            {
                "name": "egg",
                "expiration_date": datetime.date(2021, 7, 20),
            }
        ],
            ["salmon", "cheese", "egg"]
        )
    ]
)
def test_outdated_product(
        date_time: mock,
        product: list,
        expected_list: list
) -> None:
    date_time.date.today.return_value = datetime.date(2023, 10, 29)
    assert outdated_products(product) == expected_list
