from unittest import mock

import pytest

import datetime

from app.main import outdated_products


@pytest.mark.parametrize(
    "products,result",
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
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ],
            ["chicken", "duck"],
        ),
    ],
)
def test_main(products: list, result: list) -> None:
    with mock.patch("app.main.datetime") as test_datetime:
        test_datetime.date.today.return_value = datetime.date(2022, 2, 6)
        assert outdated_products(products) == result
