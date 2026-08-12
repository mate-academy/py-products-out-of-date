import datetime
from typing import List
from _pytest.monkeypatch import MonkeyPatch
from app.main import outdated_products


def test_no_outdated_products(monkeypatch: MonkeyPatch) -> None:
    class FakeDate(datetime.date):
        @classmethod
        def today(cls) -> "FakeDate":
            return cls(2022, 2, 2)

    monkeypatch.setattr(datetime, "date", FakeDate)

    products: List[dict] = [
        {
            "name": "salmon",
            "expiration_date": FakeDate(2022, 2, 10),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": FakeDate(2022, 2, 5),
            "price": 120,
        },
    ]

    assert outdated_products(products) == []


def test_one_outdated_product(monkeypatch: MonkeyPatch) -> None:
    class FakeDate(datetime.date):
        @classmethod
        def today(cls) -> "FakeDate":
            return cls(2022, 2, 2)

    monkeypatch.setattr(datetime, "date", FakeDate)

    products: List[dict] = [
        {
            "name": "salmon",
            "expiration_date": FakeDate(2022, 2, 10),
            "price": 600,
        },
        {
            "name": "duck",
            "expiration_date": FakeDate(2022, 2, 1),
            "price": 160,
        },
    ]

    assert outdated_products(products) == ["duck"]


def test_multiple_outdated_products(monkeypatch: MonkeyPatch) -> None:
    class FakeDate(datetime.date):
        @classmethod
        def today(cls) -> "FakeDate":
            return cls(2022, 2, 10)

    monkeypatch.setattr(datetime, "date", FakeDate)

    products: List[dict] = [
        {
            "name": "salmon",
            "expiration_date": FakeDate(2022, 2, 1),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": FakeDate(2022, 2, 5),
            "price": 120,
        },
        {
            "name": "duck",
            "expiration_date": FakeDate(2022, 2, 9),
            "price": 160,
        },
    ]

    assert outdated_products(products) == [
        "salmon",
        "chicken",
        "duck",
    ]


def test_expiration_date_equal_today_is_not_outdated(
    monkeypatch: MonkeyPatch,
) -> None:
    class FakeDate(datetime.date):
        @classmethod
        def today(cls) -> "FakeDate":
            return cls(2022, 2, 10)

    monkeypatch.setattr(datetime, "date", FakeDate)

    products: List[dict] = [
        {
            "name": "salmon",
            "expiration_date": FakeDate(2022, 2, 10),
            "price": 600,
        }
    ]

    assert outdated_products(products) == []


def test_expiration_date_yesterday_is_outdated(
    monkeypatch: MonkeyPatch,
) -> None:
    class FakeDate(datetime.date):
        @classmethod
        def today(cls) -> "FakeDate":
            return cls(2022, 2, 10)

    monkeypatch.setattr(datetime, "date", FakeDate)

    products: List[dict] = [
        {
            "name": "chicken",
            "expiration_date": FakeDate(2022, 2, 9),
            "price": 120,
        }
    ]

    assert outdated_products(products) == ["chicken"]
