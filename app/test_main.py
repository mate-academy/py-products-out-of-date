import pytest

import datetime

from freezegun import freeze_time

from app.main import outdated_products


@pytest.fixture
def product_list() -> list:
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
    return products


@freeze_time("2022-01-01")
def test_no_outdated_products(
        product_list: list
) -> None:
    assert outdated_products(product_list) == []


@freeze_time("2022-12-01")
def test_outdated_products(
        product_list: list
) -> None:
    assert outdated_products(product_list) == ["salmon", "chicken", "duck"]


@freeze_time("2022-02-04")
def test_one_outdated_product(
        product_list: list
) -> None:
    assert outdated_products(product_list) == ["duck"]


@freeze_time("2022-02-09")
def test_two_outdated_product(
        product_list: list
) -> None:
    assert outdated_products(product_list) == ["chicken", "duck"]
