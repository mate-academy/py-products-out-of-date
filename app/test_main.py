import pytest

from app.main import outdated_products, datetime


@pytest.fixture
def product_list() -> list:
    return [
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


def test_outdated_products(monkeypatch: pytest.MonkeyPatch,
                           product_list: list) -> None:
    real_datetime_date = datetime.date

    class MockDate:
        @staticmethod
        def today() -> datetime.date:
            return real_datetime_date(2022, 2, 2)

    monkeypatch.setattr(datetime, "date", MockDate)

    assert outdated_products(product_list) == ["duck"]


def test_no_outdated_products(monkeypatch: pytest.MonkeyPatch,
                              product_list: list) -> None:
    real_datetime_date = datetime.date

    class MockDate:
        @staticmethod
        def today() -> datetime.date:
            return real_datetime_date(2001, 11, 9)

    monkeypatch.setattr(datetime, "date", MockDate)

    assert outdated_products(product_list) == []


def test_outdated_products_today(monkeypatch: pytest.MonkeyPatch,
                                 product_list: list) -> None:
    real_datetime_date = datetime.date

    class MockDate:
        @staticmethod
        def today() -> datetime.date:
            return real_datetime_date(2022, 2, 5)

    monkeypatch.setattr(datetime, "date", MockDate)

    assert outdated_products(product_list) == ["duck"]
