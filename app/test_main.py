import pytest
import datetime

from app.main import outdated_products


@pytest.fixture(scope="module")
def list_of_products() -> list[dict]:
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


def test_no_out_of_date_products(
        list_of_products: list[dict], monkeypatch: pytest.MonkeyPatch
) -> None:
    class MockDate(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return datetime.date(2022, 1, 31)

    monkeypatch.setattr("app.main.datetime.date", MockDate)

    assert outdated_products(list_of_products) == []


def test_all_out_of_date_products(
        list_of_products: list[dict], monkeypatch: pytest.MonkeyPatch
) -> None:
    class MockDate(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return datetime.date(2022, 2, 11)

    monkeypatch.setattr("app.main.datetime.date", MockDate)

    assert outdated_products(list_of_products) == ["salmon", "chicken", "duck"]


def test_one_out_of_date_product(
        list_of_products: list[dict], monkeypatch: pytest.MonkeyPatch
) -> None:
    class MockDate(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return datetime.date(2022, 2, 2)

    monkeypatch.setattr("app.main.datetime.date", MockDate)

    assert outdated_products(list_of_products) == ["duck"]


def test_today_expiration_date(
        list_of_products: list[dict], monkeypatch: pytest.MonkeyPatch
) -> None:
    class MockDate(datetime.date):
        @classmethod
        def today(cls) -> datetime.date:
            return datetime.date(2022, 2, 1)

    monkeypatch.setattr("app.main.datetime.date", MockDate)

    assert outdated_products(list_of_products) == []
