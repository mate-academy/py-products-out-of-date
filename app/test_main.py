import pytest

import datetime
from unittest import mock

from app.main import outdated_products


@pytest.mark.parametrize(
    "products,today_test_date,expected_result",
    [
        (
            [
                {
                    "name": "Potato",
                    "expiration_date": datetime.date(2024, 1, 1),
                    "price": 27
                },
                {
                    "name": "Carrot",
                    "expiration_date": datetime.date(2024, 1, 10),
                    "price": 18
                },
                {
                    "name": "Onion",
                    "expiration_date": datetime.date(2024, 1, 11),
                    "price": 20
                },
                {
                    "name": "Apple",
                    "expiration_date": datetime.date(2024, 1, 9),
                    "price": 29
                }
            ],
            datetime.date(2024, 1, 10),
            ["Potato", "Apple"]
        )
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(
        mocked_datetime: mock.Mock,
        products: list[dict],
        today_test_date: datetime.date,
        expected_result: list
) -> None:
    mocked_datetime.date.today.return_value = today_test_date
    assert outdated_products(products) == expected_result
