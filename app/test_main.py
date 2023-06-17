from datetime import date
import pytest
from unittest import mock
from app.main import outdated_products


@pytest.fixture()
def products_list() -> list[dict]:
    return [
                {
                    "name": "salmon",
                    "expiration_date": date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": date(2022, 2, 1),
                    "price": 160
                }
        ]


@mock.patch("datetime.date")
def test_all_products_are_dated(mocked_date, products_list) -> None:
    mocked_date.today.return_value = date(2022, 2, 1)
    assert outdated_products(products_list) == []


@mock.patch("datetime.date")
def test_outdated_duck_chicken(mocked_date, products_list) -> None:
    mocked_date.today.return_value = date(2022, 2, 3)
    assert outdated_products(products_list) == ["duck"]


@mock.patch("datetime.date")
def test_outdated_duck(mocked_date, products_list) -> None:
    mocked_date.today.return_value = date(2022, 2, 6)
    assert outdated_products(products_list) == ["chicken", "duck"]


@mock.patch("datetime.date")
def test_outdated_all(mocked_date, products_list) -> None:
    mocked_date.today.return_value = date(2022, 2, 20)
    assert outdated_products(products_list) == ["salmon", "chicken", "duck"]
