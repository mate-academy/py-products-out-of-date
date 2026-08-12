import datetime
import pytest

from app.main import outdated_products


@pytest.fixture()
def products() -> list[dict]:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 11, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2023, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2023, 12, 1),
            "price": 160
        },
        {
            "name": "cherries",
            "expiration_date": datetime.date(2023, 10, 19),
            "price": 110
        },
        {
            "name": "fried potato",
            "expiration_date": datetime.date(2023, 10, 18),
            "price": 200
        }
    ]


def test_outdated_products(products: list[dict]) -> None:
    assert outdated_products(products) == ["chicken", "fried potato"]
