import datetime

from unittest import mock

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "current_date, existing_product, non_expired_product",
    [
        (
            datetime.date(2022, 2, 2),
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
        current_date: datetime.date,
        existing_product: list[dict],
        non_expired_product: list[dict]) -> None:
    with mock.patch("app.main.datetime") as mocked_datetime:
        mocked_datetime.date.today.return_value = current_date
        assert outdated_products(existing_product) == non_expired_product
