import pytest
import datetime
from app.main import outdated_products


@pytest.fixture()
def products() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date.today(),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2023, 5, 1),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2023, 5, 11),
            "price": 160
        }
    ]


def test_return_outdated_products(products: list[dict]) -> None:
    assert outdated_products(products) == ["chicken", "duck"]
