import datetime
from unittest.mock import patch

from app.main import outdated_products


class FakeDate(datetime.date):
    @classmethod
    def today(cls) -> datetime.date:
        return cls(2022, 2, 2)


def test_outdated_products() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(
                2022,
                2,
                10,
            ),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(
                2022,
                2,
                5,
            ),
            "price": 120,
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(
                2022,
                2,
                1,
            ),
            "price": 160,
        },
    ]

    with patch(
        "app.main.datetime.date",
        FakeDate,
    ):
        assert outdated_products(products) == [
            "duck",
        ]


def test_product_expires_today() -> None:
    products = [
        {
            "name": "milk",
            "expiration_date": datetime.date(
                2022,
                2,
                2,
            ),
            "price": 50,
        },
    ]

    with patch(
        "app.main.datetime.date",
        FakeDate,
    ):
        assert outdated_products(products) == []


def test_no_outdated_products() -> None:
    products = [
        {
            "name": "apple",
            "expiration_date": datetime.date(
                2022,
                2,
                10,
            ),
            "price": 30,
        },
    ]

    with patch(
        "app.main.datetime.date",
        FakeDate,
    ):
        assert outdated_products(products) == []
