import pytest
import datetime

from app.main import outdated_products

test_data = [
    {
        "name": "salmon",
        "expiration_date": datetime.date(2022, 2, 10),
        "price": 600,
    },
    {
        "name": "chicken",
        "expiration_date": datetime.date(2022, 2, 5),
        "price": 120,
    },
    {
        "name": "duck",
        "expiration_date": datetime.date(2022, 2, 1),
        "price": 160,
    },
    {
        "name": "mayo",
        "expiration_date": datetime.date(2022, 2, 2),
        "price": 160,
    },
]


def test_outdated_data(monkeypatch: pytest.MonkeyPatch) -> None:
    class MockDate(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return cls(2022, 2, 2)

    monkeypatch.setattr("app.main.datetime.date", MockDate)
    assert outdated_products(test_data) == ["duck"]
