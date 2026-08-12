import pytest

import datetime

from app.main import outdated_products


@pytest.fixture()
def products_template() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2024, 10, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2024, 9, 30),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2024, 9, 29),
            "price": 160
        }
    ]


def test_should_return_expired_products(products_template: list) -> None:
    assert outdated_products(products_template) == ["duck"]
