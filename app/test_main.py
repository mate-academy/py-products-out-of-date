import datetime

import pytest

from _pytest.monkeypatch import MonkeyPatch

import app

from app.main import outdated_products


class FakeDate(datetime.date):
    @classmethod
    def today(cls) -> datetime.date:
        return datetime.date(2026, 1, 1)


@pytest.fixture(scope="function")
def mocked_datetime_today(monkeypatch: MonkeyPatch) -> None:

    monkeypatch.setattr(app.main.datetime, "date", FakeDate)


@pytest.fixture(scope="function")
def products_list() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2026, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2026, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2026, 2, 1),
            "price": 160
        }
    ]


def test_outdated_products_when_list_is_empty() -> None:
    assert outdated_products([]) == []


def test_outdated_products_when_products_arent_outdated(
        products_list: list,
        mocked_datetime_today: None
) -> None:
    assert outdated_products(products_list) == []


def test_outdated_products_when_all_products_are_outdated(
        products_list: list,
        mocked_datetime_today: None
) -> None:

    for product in products_list:
        product["expiration_date"] = datetime.date(2025, 9, 5)

    assert outdated_products(products_list) == ["salmon", "chicken", "duck"]


def test_outdated_products_when_one_product_is_outdated(
        products_list: list,
        mocked_datetime_today: None
) -> None:
    products_list[1]["expiration_date"] = datetime.date(2025, 10, 20)

    assert outdated_products(products_list) == ["chicken"]


def test_outdated_products_when_expiration_date_is_today(
        products_list: list,
        mocked_datetime_today: None
) -> None:
    products_list[0]["expiration_date"] = datetime.date(2026, 1, 1)

    assert outdated_products(products_list) == []


def test_outdated_products_when_expiration_date_is_yesterday(
        products_list: list,
        mocked_datetime_today: None
) -> None:
    products_list[2]["expiration_date"] = datetime.date(2025, 12, 31)

    assert outdated_products(products_list) == ["duck"]
