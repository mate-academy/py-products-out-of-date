from __future__ import annotations
import datetime

from app.main import outdated_products


def test_function_should_returns_only_expired_product() -> None:
    class MockedDate(datetime.date):
        @classmethod
        def today(cls) -> MockedDate:
            return cls(2024, 7, 15)

    datetime.date = MockedDate
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2024, 7, 16),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2024, 7, 15),
            "price": 500
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2024, 7, 14),
            "price": 500
        }
    ]
    assert outdated_products(products) == ["duck"]
