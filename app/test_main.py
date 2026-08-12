from __future__ import annotations
from typing import Any
import datetime as _dt

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "products, today, expected",
    [
        (
            [
                {
                    "name": "Milk",
                    "expiration_date": _dt.date(2023, 1, 1),
                    "price": 100,
                },
                {
                    "name": "Bread",
                    "expiration_date": _dt.date(2025, 1, 1),
                    "price": 50,
                },
                {
                    "name": "Cheese",
                    "expiration_date": _dt.date(2022, 12, 31),
                    "price": 200,
                },
            ],
            _dt.date(2024, 1, 1),
            ["Milk", "Cheese"],
        ),
        (
            [
                {
                    "name": "Yogurt",
                    "expiration_date": _dt.date(2025, 1, 8),
                    "price": 80,
                },
                {
                    "name": "Butter",
                    "expiration_date": _dt.date(2025, 1, 9),
                    "price": 120,
                },
            ],
            _dt.date(2025, 1, 9),
            ["Yogurt"],
        ),
        (
            [
                {
                    "name": "Eggs",
                    "expiration_date": _dt.date(2024, 12, 31),
                    "price": 150,
                },
            ],
            _dt.date(2024, 1, 1),
            [],
        ),
    ],
)
def test_outdated_products(
    monkeypatch: pytest.MonkeyPatch,
    products: list[dict[str, Any]],
    today: _dt.date,
    expected: list[str]
) -> None:
    class FrozenDate(_dt.date):
        @classmethod
        def today(cls) -> _dt.date:
            return today

    monkeypatch.setattr("app.main.datetime.date", FrozenDate)

    assert outdated_products(products) == expected
