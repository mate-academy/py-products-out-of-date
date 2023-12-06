from unittest import mock

import pytest

import datetime

from app.main import outdated_products


@pytest.mark.parametrize(
    "products, result",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2023, 2, 9),
                    "price": 600
                },
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 9),
                    "price": 600
                }
            ],
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 9),
                    "price": 600
                }
            ]
        ),
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2021, 2, 10),
                    "price": 600
                },
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 9),
                    "price": 600
                },
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 1, 19),
                    "price": 600
                }
            ],
            []
        )
    ]
)
@mock.patch("datetime.date.today", value=datetime.date(2022, 2, 10))
def test_outdated_products(
        mocked_today: any,
        products: list[dict],
        result: list[dict]) -> None:

    assert (
        outdated_products(products) == result
    )
    mocked_today.assert_called()
