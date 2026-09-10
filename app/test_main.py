import datetime

from app.main import outdated_products


def test_outdated_products(monkeypatch) -> None:
    class MockDate(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return cls(2022, 2, 2)

    monkeypatch.setattr("app.main.date", MockDate)

    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 120,
        },
    ]

    result = outdated_products(products)
    assert result == ["chicken"]
