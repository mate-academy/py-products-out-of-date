import datetime
from unittest import mock

import pytest

from app.main import outdated_products


TODAY = datetime.date(2022, 2, 2)
BEFORE_ALL_EXPIRATIONS = datetime.date(2022, 1, 1)
AFTER_ALL_EXPIRATIONS = datetime.date(2022, 3, 1)


@pytest.fixture()
def products() -> list[dict]:
    return [
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
        },
    ]


@mock.patch("datetime.date")
def test_should_return_only_outdated_products(
        mocked_date: mock.MagicMock,
        products: list[dict],
) -> None:
    mocked_date.today.return_value = TODAY
    assert outdated_products(products) == ["duck"]


@mock.patch("datetime.date")
def test_product_expiring_today_is_not_outdated(
        mocked_date: mock.MagicMock,
        products: list[dict],
) -> None:
    mocked_date.today.return_value = TODAY
    assert "chicken" not in outdated_products(products)


@mock.patch("datetime.date")
def test_product_expired_yesterday_is_outdated(
        mocked_date: mock.MagicMock,
        products: list[dict],
) -> None:
    mocked_date.today.return_value = TODAY
    assert "duck" in outdated_products(products)


@mock.patch("datetime.date")
def test_should_return_empty_list_when_nothing_is_outdated(
        mocked_date: mock.MagicMock,
        products: list[dict],
) -> None:
    mocked_date.today.return_value = BEFORE_ALL_EXPIRATIONS
    assert outdated_products(products) == []


@mock.patch("datetime.date")
def test_should_return_all_products_when_all_are_outdated(
        mocked_date: mock.MagicMock,
        products: list[dict],
) -> None:
    mocked_date.today.return_value = AFTER_ALL_EXPIRATIONS
    assert outdated_products(products) == ["salmon", "chicken", "duck"]
