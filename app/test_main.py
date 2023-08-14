from app.main import outdated_products
import datetime
import pytest


@pytest.fixture()
def first_product_template() -> dict:
    return {
        "name": "chicken",
        "expiration_date": datetime.date(2023, 8, 13),
        "price": 120,
    }


@pytest.fixture()
def second_product_template() -> dict:
    return {
        "name": "duck",
        "expiration_date": datetime.date(2023, 8, 14),
        "price": 160,
    }


@pytest.fixture()
def list_to_test(
    first_product_template: dict, second_product_template: dict
) -> list:
    return [
        first_product_template,
        second_product_template,
    ]


def test_correct_function_result(list_to_test: list) -> None:
    assert outdated_products(list_to_test) == ["chicken"]
