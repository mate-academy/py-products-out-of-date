import pytest
from app.main import outdated_products
from datetime import date


@pytest.fixture
def products_list() -> list:
    products_list = [
        {"name": "salmon", "expiration_date": date(2026, 1, 28), "price": 600},
        {"name": "chicken", "expiration_date": date(2022, 1, 29),
         "price": 120},
        {"name": "duck", "expiration_date": date(2022, 1, 27), "price": 160},
    ]
    return products_list


def test_two_products_out_of_date(products_list: list) -> None:

    assert outdated_products(products_list) == ["chicken", "duck"]


def test_all_products_out_of_date() -> None:
    products_list = [
        {"name": "salmon", "expiration_date": date(2026, 1, 27), "price": 600},
        {"name": "chicken", "expiration_date": date(2022, 1, 27),
         "price": 120},
        {"name": "duck", "expiration_date": date(2022, 1, 27), "price": 160},
    ]
    assert outdated_products(products_list) == ["salmon", "chicken", "duck"]
