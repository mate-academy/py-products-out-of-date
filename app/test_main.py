import datetime
import pytest
from app.main import outdated_products


def test_outdated_products_logic(monkeypatch: pytest.MonkeyPatch) -> None:
    fixed_today = datetime.date(2022, 2, 2)

    class MockDate(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return fixed_today
    monkeypatch.setattr("app.main.datetime.date", MockDate)
    products = [
        {"name": "duck", "expiration_date": datetime.date(2022, 2, 1)},
        {"name": "chicken", "expiration_date": datetime.date(2022, 2, 2)},
        {"name": "salmon", "expiration_date": datetime.date(2022, 2, 3)},
    ]
    result = outdated_products(products)
    assert result == ["duck"], (
        f"Expected ['duck'], but got {result}. "
        "Ensure products expiring today are NOT considered outdated."
    )


def test_outdated_products_empty_list() -> None:
    assert outdated_products([]) == []


def test_outdated_products_all_expired(
        monkeypatch: pytest.MonkeyPatch
) -> None:
    fixed_today = datetime.date(2022, 2, 2)

    class MockDate(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return fixed_today
    monkeypatch.setattr("app.main.datetime.date", MockDate)
    products = [
        {"name": "old_bread", "expiration_date": datetime.date(2022, 1, 1)},
        {"name": "old_milk", "expiration_date": datetime.date(2022, 1, 31)},
    ]
    assert outdated_products(products) == ["old_bread", "old_milk"]
