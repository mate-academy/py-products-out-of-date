from app.main import outdated_products
import app.main as main
import datetime
from _pytest.monkeypatch import MonkeyPatch


def test_time(monkeypatch: MonkeyPatch) -> None:
    class FakeDate(datetime.date):
        @classmethod
        def today(cls) -> "FakeDate":
            return cls(2022, 2, 2)

    monkeypatch.setattr(main.datetime, "date", FakeDate)

    products = [
        {
            "name": "expired",
            "expiration_date": FakeDate(2021, 1, 12),
            "price": 100
        },
        {
            "name": "today",
            "expiration_date": FakeDate(2022, 2, 2),
            "price": 100
        },
        {
            "name": "future",
            "expiration_date": FakeDate(2022, 3, 1),
            "price": 100
        },
    ]

    expected = ["expired"]
    result = outdated_products(products)

    assert set(result) == set(expected)


def test_less(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(main.datetime, "date", datetime.date)

    products = []
    result = outdated_products(products)
    assert result == []
