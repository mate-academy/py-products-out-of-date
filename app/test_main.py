import datetime
from _pytest.monkeypatch import MonkeyPatch
import app.main as main


def _make_prod(name: str, year: int, month: int, day: int) -> dict:
    return {
        "name": name,
        "expiration_date": datetime.date(year, month, day),
        "price": 100
    }


def test_no_outdated(monkeypatch: MonkeyPatch) -> None:
    class FakeDate(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return cls(2025, 11, 4)
    monkeypatch.setattr(main.datetime,
                        "date", FakeDate)

    products = [
        _make_prod("salmon", 2025, 11, 10),
        _make_prod("chicken", 2025, 11, 14),
    ]
    assert main.outdated_products(products) == []


def test_outdated(monkeypatch: MonkeyPatch) -> None:
    class FakeDate(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return cls(2025, 11, 4)
    monkeypatch.setattr(main.datetime,
                        "date", FakeDate)
    products = [
        _make_prod("milk", 2025, 9, 30),
        _make_prod("ham", 2025, 10, 31),
    ]
    assert main.outdated_products(products) == ["milk", "ham"]


def test_expiration_today_not_outdated(monkeypatch: MonkeyPatch) -> None:
    class FakeDate(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return cls(2025, 11, 4)

    monkeypatch.setattr(main.datetime, "date", FakeDate)

    products = [
        _make_prod("yogurt", 2025, 11, 4),
        _make_prod("bread", 2025, 11, 3),
    ]
    assert main.outdated_products(products) == ["bread"]
