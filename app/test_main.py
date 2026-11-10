import datetime
import pytest

from app.main import outdated_products

RealDate = datetime.date


class MockDate:
    @classmethod
    def today(cls) -> RealDate:
        return RealDate(2022, 2, 2)


def test_outdated_products(monkeypatch: pytest.MonkeyPatch) -> None:
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

    monkeypatch.setattr("datetime.date", MockDate)

    result = outdated_products(products)
    assert result == ["duck"]


def test_products_expire_today(monkeypatch: pytest.MonkeyPatch) -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]

    monkeypatch.setattr("datetime.date", MockDate)

    result = outdated_products(products)
    assert "chicken" not in result
