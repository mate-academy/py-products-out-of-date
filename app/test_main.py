# app/test_main.py
import datetime
import pytest
from unittest.mock import patch

from app.main import outdated_products


@pytest.mark.parametrize(
    "today,products,expected",
    [
        (
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10), "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5), "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1), "price": 160
                },
            ],
            ["duck"],
        ),
        (
            datetime.date(2022, 5, 10),
            [
                {
                    "name": "juice",
                    "expiration_date": datetime.date(2022, 5, 10), "price": 50
                },
                {
                    "name": "cheese",
                    "expiration_date": datetime.date(2022, 5, 11), "price": 200
                },
            ],
            [],
        ),
        (
            datetime.date(2022, 3, 1),
            [
                {
                    "name": "apple",
                    "expiration_date": datetime.date(2022, 2, 10), "price": 10
                },
                {
                    "name": "bread",
                    "expiration_date": datetime.date(2022, 2, 28), "price": 20
                },
            ],
            ["apple", "bread"],
        ),
        (
            datetime.date(2022, 1, 1),
            [],
            [],
        ),
    ],
)
def test_outdated_products_with_patch(
        today: datetime.date,
        products: list,
        expected: list
) -> None:
    class FixedDate(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return today

    with patch("app.main.datetime.date", FixedDate):
        assert outdated_products(products) == expected
