import datetime
from pytest import MonkeyPatch
from app.main import outdated_products


class MockDate(datetime.date):
    @classmethod
    def today(cls) -> datetime.date:
        return cls(2022, 2, 2)


def test_should_return_outdated_products(
        monkeypatch: MonkeyPatch,) -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]

    monkeypatch.setattr(
        datetime,
        "date",
        MockDate
    )

    assert outdated_products(products) == ["duck"]


def test_should_not_return_not_outdated_products(
        monkeypatch: MonkeyPatch,) -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 160
        }
    ]

    monkeypatch.setattr(
        datetime,
        "date",
        MockDate
    )

    assert outdated_products(products) == []


def test_should_not_return_fresh_products(
        monkeypatch: MonkeyPatch,) -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 6),
            "price": 160
        }
    ]

    monkeypatch.setattr(
        datetime,
        "date",
        MockDate
    )

    assert outdated_products(products) == []
