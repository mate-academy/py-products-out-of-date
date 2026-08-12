import pytest
import datetime
from app.main import outdated_products
from unittest import mock
from typing import Any


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
            ["duck"]
        ),
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
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 160
                }
            ],
            []
        ),
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 1, 30),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 1, 31),
                    "price": 160
                }
            ],
            ["salmon", "chicken", "duck"]
        )
    ]
)
def test_outdated_products(products: list, result: list) -> None:
    class MyDate(datetime.date):
        @classmethod
        def today(cls) -> Any:
            return cls(2022, 2, 2)

    with mock.patch("app.main.datetime.date", MyDate):
        result_outdated_products = outdated_products(products)

    assert result_outdated_products == result
