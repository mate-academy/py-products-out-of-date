import datetime

import pytest
from pytest import MonkeyPatch

from app.main import outdated_products


@pytest.mark.parametrize(
    "today", [datetime.date(2024, 3, 1), datetime.date(2025, 1, 1)]
)
def test_expiry_boundary_with_mocked_today(
    monkeypatch: MonkeyPatch, today: datetime.date
) -> None:
    class FixedDate(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return today

    monkeypatch.setattr("app.main.datetime.date", FixedDate)
    products = [
        {"name": "yesterday",
         "expiration_date": today - datetime.timedelta(days=1)},
        {"name": "today", "expiration_date": today},
        {"name": "tomorrow",
         "expiration_date": today + datetime.timedelta(days=1)},
        {"name": "older",
         "expiration_date": today - datetime.timedelta(days=10)},
    ]
    original_products = [product.copy() for product in products]
    assert outdated_products(products) == ["yesterday", "older"]
    assert products == original_products


def test_empty_products() -> None:
    assert outdated_products([]) == []
