import datetime

import pytest

from app.main import outdated_products


class MockDate(datetime.date):
    @classmethod
    def today(cls) -> "MockDate":
        return cls(2022, 2, 2)


def test_returns_only_products_expired_before_today(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
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


def test_product_with_expiration_date_equal_today_is_not_outdated(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(datetime, "date", MockDate)

    products = [
        {
            "name": "milk",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 40,
        }
    ]

    assert outdated_products(products) == []


def test_product_with_expiration_date_equal_yesterday_is_outdated(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(datetime, "date", MockDate)

    products = [
        {
            "name": "bread",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 25,
        }
    ]

    assert outdated_products(products) == ["bread"]
