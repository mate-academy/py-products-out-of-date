import datetime

from unittest import mock

import pytest

from app import main


@pytest.mark.parametrize(
    "current_date, products, expected_result",
    [
        pytest.param(
            datetime.date(2022, 2, 9),
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
            ["chicken", "duck"]
        ),
        pytest.param(
            datetime.date(2022, 2, 9),
            [],
            []
        )
    ]
)
def test_outdated_products(
    current_date: datetime,
    products: list,
    expected_result: list
) -> None:
    with mock.patch("app.main.datetime") as mocked_date:
        mocked_date.date.today.return_value = current_date
        assert main.outdated_products(products) == expected_result
