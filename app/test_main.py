import datetime
from typing import List, Dict
from unittest import mock
import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "today, products, expected_outdated_products",
    [
        (
            datetime.date(2022, 2, 3),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10)
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5)
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1)
                }
            ],
            ["duck"]
        )
    ]
)
def test_outdated_products(
        today: datetime.date,
        products: List[Dict],
        expected_outdated_products: List[Dict]) -> None:

    with mock.patch("app.main.datetime") as mocked_datetime:
        mocked_datetime.date.today.return_value = today
        assert outdated_products(products) == expected_outdated_products
