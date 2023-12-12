import datetime

from unittest import mock

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "today, product, expected_result",
    [
        (
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                }
            ],
            []
        ),
        (
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 600
                }
            ],
            []
        ),
        (
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 600
                }
            ],
            ["duck"]
        )
    ],
    ids=[
        "expiration date > today date - []",
        "expiration date > today date - []",
        "expiration date < today date - ['duck']"
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(
        mocked_datetime: callable,
        today: datetime.date,
        product: list,
        expected_result: list
) -> None:
    mocked_datetime.date.today.return_value = today

    assert outdated_products(product) == expected_result
