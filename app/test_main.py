import datetime
from _pytest.monkeypatch import MonkeyPatch
from app.main import outdated_products
import app.main


def test_outdated_products_with_fixed_today_2022_02_02(
    monkeypatch: MonkeyPatch,
) -> None:
    real_date = datetime.date

    class FakeDate:
        @staticmethod
        def today() -> datetime.date:
            return real_date(2022, 2, 2)

    monkeypatch.setattr(app.main.datetime, "date", FakeDate)

    products: list[dict[str, object]] = [
        {
            "name": "salmon",
            "expiration_date": real_date(2022, 2, 10),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": real_date(2022, 2, 5),
            "price": 120,
        },
        {
            "name": "duck",
            "expiration_date": real_date(2022, 2, 1),
            "price": 160,
        },
    ]

    assert outdated_products(products) == ["duck"]


def test_outdated_products_expiring_today_is_not_outdated(
    monkeypatch: MonkeyPatch,
) -> None:
    real_date = datetime.date

    class FakeDate:
        @staticmethod
        def today() -> datetime.date:
            return real_date(2022, 2, 2)

    monkeypatch.setattr(app.main.datetime, "date", FakeDate)

    products: list[dict[str, object]] = [
        {
            "name": "milk",
            "expiration_date": real_date(2022, 2, 2),
            "price": 50,
        },
        {
            "name": "bread",
            "expiration_date": real_date(2022, 2, 1),
            "price": 25,
        },
    ]

    assert outdated_products(products) == ["bread"]


def test_outdated_products_no_outdated(monkeypatch: MonkeyPatch) -> None:
    real_date = datetime.date

    class FakeDate:
        @staticmethod
        def today() -> datetime.date:
            return real_date(2022, 2, 2)

    monkeypatch.setattr(app.main.datetime, "date", FakeDate)

    products: list[dict[str, object]] = [
        {
            "name": "apple",
            "expiration_date": real_date(2022, 2, 2),
            "price": 10,
        },
        {
            "name": "banana",
            "expiration_date": real_date(2022, 2, 3),
            "price": 20,
        },
    ]

    assert outdated_products(products) == []


def test_outdated_products_multiple_outdated(
    monkeypatch: MonkeyPatch,
) -> None:
    real_date = datetime.date

    class FakeDate:
        @staticmethod
        def today() -> datetime.date:
            return real_date(2023, 1, 10)

    monkeypatch.setattr(app.main.datetime, "date", FakeDate)

    products: list[dict[str, object]] = [
        {
            "name": "eggs",
            "expiration_date": real_date(2023, 1, 1),
            "price": 70,
        },
        {
            "name": "cheese",
            "expiration_date": real_date(2023, 1, 10),
            "price": 200,
        },
        {
            "name": "ham",
            "expiration_date": real_date(2023, 1, 9),
            "price": 180,
        },
    ]

    assert outdated_products(products) == ["eggs", "ham"]
