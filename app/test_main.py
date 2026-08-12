import datetime
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "products, expected",
    [
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2023, 7, 24)
                }
            ],
            [],
            id="expiration day is today's date, not outdated, empty list"
        ),
        pytest.param(
            [
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2023, 7, 23)
                }
            ],
            ["chicken"],
            id="expiration day is yesterday's date, outdated, included to list"
        ),
        pytest.param(
            [
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2023, 6, 19)
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2023, 7, 20),
                    "price": 120
                },
            ],
            ["duck", "chicken"],
            id="should contain all outdated products"
        )
    ]
)
def test_outdated_products(products: list[dict], expected: list[str]) -> None:
    with mock.patch("app.main.datetime") as mocked_date:
        mocked_date.date.today.return_value = datetime.date(2023, 7, 24)
        assert outdated_products(products) == expected
