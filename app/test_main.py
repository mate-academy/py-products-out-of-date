import datetime as _dt
from typing import List, Dict
from _pytest.monkeypatch import MonkeyPatch
import app.main as m
from app.main import outdated_products

dt_date = _dt.date


def _patch_today(monkeypatch: MonkeyPatch, today: _dt.date) -> None:
    class FixedDate(_dt.date):
        @classmethod
        def today(cls) -> "FixedDate":
            return cls(today.year, today.month, today.day)

    monkeypatch.setattr(m, "date", FixedDate, raising=False)
    monkeypatch.setattr(m.datetime, "date", FixedDate, raising=False)


def _sample_products() -> List[Dict]:
    return [
        {
            "name": "salmon",
            "expiration_date": dt_date(2022, 2, 10),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": dt_date(2022, 2, 5),
            "price": 120,
        },
        {
            "name": "duck",
            "expiration_date": dt_date(2022, 2, 1),
            "price": 160,
        },
    ]


def test_single_outdated_matches_example(monkeypatch: MonkeyPatch) -> None:
    _patch_today(monkeypatch, dt_date(2022, 2, 2))
    products = _sample_products()
    assert outdated_products(products) == ["duck"]


def test_no_outdated_when_equal_is_not_outdated(
    monkeypatch: MonkeyPatch,
) -> None:
    _patch_today(monkeypatch, dt_date(2022, 2, 1))
    products = _sample_products()
    assert outdated_products(products) == []


def test_multiple_outdated_preserve_order(
    monkeypatch: MonkeyPatch,
) -> None:
    _patch_today(monkeypatch, dt_date(2022, 2, 11))
    products = _sample_products()
    assert outdated_products(products) == ["salmon", "chicken", "duck"]


def test_empty_input_returns_empty(monkeypatch: MonkeyPatch) -> None:
    _patch_today(monkeypatch, dt_date(2022, 2, 2))
    assert outdated_products([]) == []
