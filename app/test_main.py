import pytest
import unittest.mock
import datetime
from typing import Callable, Any
from app.main import outdated_products


@pytest.mark.parametrize(
    "today_date,products,expected",
    [
        (
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                },
            ],
            ["duck"],
        ),
        (
            datetime.date(2022, 2, 2),
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
            ],
            [],
        ),
        (
            datetime.date(2022, 2, 10),
            [
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                },
                {
                    "name": "milk",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 50,
                }
            ],
            ["duck", "milk"],
        ),
        (
            datetime.date(2022, 2, 10),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
            ],
            [],
        )
    ]
)
@unittest.mock.patch("app.main.datetime.date")
def test_main(
    mock_date: Callable,
    today_date: Any,
    products: list,
    expected: list
) -> None:
    mock_date.today.return_value = today_date

    assert outdated_products(products) == expected
