import datetime

from app import main


def test_outdated_products(monkeypatch) -> None:
    real_date = datetime.date

    class FakeDate(datetime.date):
        @classmethod
        def today(cls):
            return cls(2022, 2, 2)

    monkeypatch.setattr(main.datetime, "date", FakeDate)

    products = [
        {
            "name": "salmon",
            "expiration_date": real_date(2022, 2, 10),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": real_date(2022, 2, 2),
            "price": 120,
        },
        {
            "name": "duck",
            "expiration_date": real_date(2022, 2, 1),
            "price": 160,
        },
    ]

    assert main.outdated_products(products) == ["duck"]
