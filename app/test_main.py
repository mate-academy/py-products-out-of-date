import pytest
import datetime
from app.main import outdated_products


@pytest.fixture()
def data() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2025, 4, 10),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2025, 4, 17),
            "price": 120,
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2025, 4, 18),
            "price": 160,
        },
    ]


def test_outdated_products(data: list) -> None:
    assert outdated_products(data) == ["salmon", "chicken"]
