import pytest
import datetime
from unittest.mock import patch

from app.main import outdated_products


@pytest.fixture
def test_data() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2024, 4, 8),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2024, 4, 9),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2024, 4, 10),
            "price": 160
        }
    ]


class MockedDate(datetime.date):
    @classmethod
    def today(cls) -> datetime.date:
        return cls(2024, 4, 9)


@patch("datetime.date", new=MockedDate)
def test_outdated_products(test_data: list) -> None:
    assert outdated_products(test_data) == ["salmon"]
