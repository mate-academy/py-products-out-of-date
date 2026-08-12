import pytest
import datetime
from unittest.mock import patch
from app.main import outdated_products


@pytest.fixture()
def data_test() -> any:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2024, 4, 18),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2024, 4, 19),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2024, 4, 20),
            "price": 160
        }
    ]


class DateMoked(datetime.date):
    @classmethod
    def today(cls) -> datetime.date:
        return cls(2024, 4, 19)


@patch("datetime.date", DateMoked)
def test_for_outdated_products(data_test: list) -> None:
    assert outdated_products(data_test) == ["salmon"]
