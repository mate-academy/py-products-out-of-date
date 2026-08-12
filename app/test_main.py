import datetime

import pytest

from app.main import outdated_products


@pytest.fixture()
def products() -> list:
    return [
        {
            "name": "yogurt",
            "expiration_date": (datetime.date.today()
                                - datetime.timedelta(days=1)),
            "price": 160,
        },
        {
            "name": "salmon",
            "expiration_date": datetime.date(2024, 12, 19),
            "price": 600,
        },
        {
            "name": "orange",
            "expiration_date": datetime.date.today(),
            "price": 160
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2024, 12, 20),
            "price": 120,
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2024, 12, 1),
            "price": 160
        },
    ]


def test_outdated_products(products: list) -> None:
    assert outdated_products(products) == ["yogurt", "duck"]
