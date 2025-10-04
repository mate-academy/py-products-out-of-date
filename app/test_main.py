import datetime
from pytest import MonkeyPatch
from app.main import outdated_products


def test_outdated_products_with_mixed_dates(monkeypatch: MonkeyPatch) -> None:
    class MockDate(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return cls(2022, 2, 2)

    monkeypatch.setattr(datetime, "date", MockDate)

    products = [
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
    ]

    assert outdated_products(products) == ["duck"]


def test_outdated_products_all_expired(monkeypatch: MonkeyPatch) -> None:
    class MockDate(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return cls(2022, 2, 5)

    monkeypatch.setattr(datetime, "date", MockDate)

    products = [
        {
            "name": "milk",
            "expiration_date": datetime.date(2022, 1, 1),
            "price": 50,
        },
        {
            "name": "cheese",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 200,
        },
    ]

    assert outdated_products(products) == ["milk", "cheese"]


def test_outdated_products_none_expired(monkeypatch: MonkeyPatch) -> None:
    class MockDate(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return cls(2022, 2, 1)

    monkeypatch.setattr(datetime, "date", MockDate)

    products = [
        {
            "name": "apple",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 5,
        },
        {
            "name": "banana",
            "expiration_date": datetime.date(2022, 2, 3),
            "price": 7,
        },
    ]

    assert outdated_products(products) == []


def test_outdated_products_on_today_date(monkeypatch: MonkeyPatch) -> None:
    class MockDate(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return cls(2022, 2, 3)

    monkeypatch.setattr(datetime, "date", MockDate)

    products = [
        {
            "name": "bread",
            "expiration_date": datetime.date(2022, 2, 3),
            "price": 15,
        }
    ]

    assert outdated_products(products) == []
