import datetime
from unittest import mock

from app.main import outdated_products


class FakeDate(datetime.date):
    @classmethod
    def today(cls) -> datetime.date:
        return cls(2022, 2, 24)


@mock.patch("app.main.datetime.date", FakeDate)
def test_outdated_products() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 23),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 24),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 28),
            "price": 160
        },
    ]

    result = outdated_products(products)

    assert result == ["salmon"], "Salmon is outdated"


@mock.patch("app.main.datetime.date", FakeDate)
def test_fresh_products() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 25),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 24),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 28),
            "price": 160
        },
    ]

    assert outdated_products(products) == []
