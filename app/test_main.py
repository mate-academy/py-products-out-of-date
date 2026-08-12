import datetime
from app import main
from app.main import outdated_products
from typing import Self
from pytest import MonkeyPatch
import pytest


def test_outdated_products_filters_correctly(
        monkeypatch: pytest.MonkeyPatch
) -> None:
    products = [
        {
            "name": "Milk",
            "expiration_date": datetime.date(2023, 10, 1),
            "price": 50,
        },
        {
            "name": "Bread",
            "expiration_date": datetime.date(2023, 10, 5),
            "price": 20,
        },
        {
            "name": "Cheese",
            "expiration_date": datetime.date(2023, 10, 10),
            "price": 100,
        },
    ]

    fixed = datetime.date(2023, 10, 5)

    class MockDate(datetime.date):
        @classmethod
        def today(cls) -> Self:
            return fixed

    class MockDatetime:
        date = MockDate
    monkeypatch.setattr(main, "datetime", MockDatetime)
    result = outdated_products(products)
    assert result == ["Milk"]


def test_outdated_products_empty_list(monkeypatch: pytest.MonkeyPatch) -> None:
    fixed = datetime.date(2023, 10, 5)

    class MockDate(datetime.date):
        @classmethod
        def today(cls) -> Self:
            return fixed

    class MockDatetime:
        date = MockDate
    monkeypatch.setattr(main, "datetime", MockDatetime)
    assert outdated_products([]) == []


def test_outdated_products_boundary_case(
        monkeypatch: pytest.MonkeyPatch
) -> None:
    fixed = datetime.date(2023, 10, 5)
    products = [{"name": "Today", "expiration_date": fixed, "price": 10}]

    class MockDate(datetime.date):
        @classmethod
        def today(cls) -> Self:
            return fixed

    class MockDatetime:
        date = MockDate
    monkeypatch.setattr(main, "datetime", MockDatetime)
    # expiration_date == today is NOT outdated
    assert outdated_products(products) == []


def test_outdated_products_all_or_none(monkeypatch: MonkeyPatch) -> None:
    fixed = datetime.date(2023, 10, 5)

    class MockDate(datetime.date):
        @classmethod
        def today(cls) -> Self:
            return fixed

    class MockDatetime:
        date = MockDate
    monkeypatch.setattr(main, "datetime", MockDatetime)
    expired = [
        {
            "name": "Old1",
            "expiration_date": datetime.date(2023, 1, 1),
            "price": 10,
        },
        {
            "name": "Old2",
            "expiration_date": datetime.date(2023, 9, 30),
            "price": 20,
        },
    ]

    assert outdated_products(expired) == ["Old1", "Old2"]
    fresh = [
        {
            "name": "New1",
            "expiration_date": datetime.date(2023, 10, 5),
            "price": 10,
        },
        {
            "name": "New2",
            "expiration_date": datetime.date(2024, 1, 1),
            "price": 20,
        },
    ]

    assert outdated_products(fresh) == []
