import pytest
import datetime
from app.main import outdated_products


def test_outdated_products(monkeypatch: pytest.MonkeyPatch) -> None:
    fake_datetime = type(
        "FakeDatetime",
        (),
        {
            "date": type(
                "FakeDate",
                (),
                {"today": lambda: datetime.date(2022, 2, 2)})}
    )

    monkeypatch.setattr("app.main.datetime", fake_datetime)

    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 600
        },
        {
            "name": "kovbasa",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 700
        },
        {
            "name": "cookies",
            "expiration_date": datetime.date(2022, 2, 3),
            "price": 1000
        }
    ]

    assert outdated_products(products) == ["salmon"]
