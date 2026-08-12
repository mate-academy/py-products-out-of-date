import pytest
from typing import Callable
from app.main import outdated_products
from unittest import mock


@pytest.fixture()
def products() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": "2022-02-02",
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": "2022-01-31",
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": "2022-02-01",
            "price": 160
        }
    ]


@mock.patch("app.main.datetime.date")
def test_expiration_yesterday(
        mocked_today: Callable,
        products: list
) -> None:
    mocked_today.today.return_value = "2022-02-01"
    assert outdated_products(products) == ["chicken"]


@mock.patch("app.main.datetime.date")
def test_expiration_two_days(
        mocked_today: Callable,
        products: list
) -> None:
    mocked_today.today.return_value = "2022-01-31"
    assert outdated_products(products) == []


@mock.patch("app.main.datetime.date")
def test_no_expiration(
        mocked_today: Callable,
        products: list
) -> None:
    mocked_today.today.return_value = "2022-02-02"
    assert outdated_products(products) == ["chicken", "duck"]
