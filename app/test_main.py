from typing import List, Dict, Any
import datetime
from pytest import MonkeyPatch

from app.main import outdated_products


class FakeDate(datetime.date):

    @classmethod
    def today(cls) -> "FakeDate":
        return cls(2022, 2, 2)


def test_expiration_day_today_not_outdated(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(datetime, "date", FakeDate)

    products: List[Dict[str, Any]] = [
        {
            "name": "milk",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 10,
        }
    ]

    assert outdated_products(products) == []


def test_expiration_day_yesterday_outdated(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(datetime, "date", FakeDate)

    products: List[Dict[str, Any]] = [
        {
            "name": "milk",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 10,
        }
    ]

    assert outdated_products(products) == ["milk"]
