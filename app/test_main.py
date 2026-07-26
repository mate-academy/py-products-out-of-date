import datetime

from _pytest.monkeypatch import MonkeyPatch

from app import main


def test_outdated_products(monkeypatch: MonkeyPatch) -> None:
    class MockDate(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return cls(2022, 2, 2)

    monkeypatch.setattr(main.datetime, "date", MockDate)

    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 120,
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 3),
            "price": 160,
        },
    ]
    result = main.outdated_products(products)

    assert result == ["salmon"]
