import datetime

from unittest import mock

import pytest

from app import main


@pytest.mark.parametrize(
    "current_date, products, expected_result",
    [
        pytest.param(
            datetime.date(1997, 12, 5),
            [
                {
                    "name": "buck",
                    "expiration_date": datetime.date(1997, 12, 10),
                    "price": 750
                },
                {
                    "name": "ser",
                    "expiration_date": datetime.date(1992, 8, 30),
                    "price": 1000
                },
                {
                    "name": "sunny",
                    "expiration_date": datetime.date(1996, 9, 9),
                    "price": 900
                }
            ],
            ["ser", "sunny"]
        ),
        pytest.param(
            datetime.date(1997, 12, 5),
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
