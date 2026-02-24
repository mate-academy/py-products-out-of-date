import datetime

from _pytest.monkeypatch import MonkeyPatch

from app.main import outdated_products


class MockDate(datetime.date):
    @classmethod
    def today(cls) -> datetime.date:
        return cls(2022, 2, 2)


def test_outdated_products(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(datetime, "date", MockDate)

    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]
    assert outdated_products(products) == ["duck"]


def test_expiration_today_not_outdated(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(datetime, "date", MockDate)
    products = [
        {
            "name": "yogurt",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 40,
        }
    ]
    assert outdated_products(products) == []
