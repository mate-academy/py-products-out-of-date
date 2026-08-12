import pytest
from unittest import mock
from app.main import outdated_products
import datetime


@pytest.fixture
def product_template() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2032, 2, 10),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2032, 2, 5),
            "price": 120,
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2032, 2, 1),
            "price": 160,
        },
    ]


@mock.patch("app.main.datetime")
def test_one_outdated_product(
    mocked_time: mock.Mock, product_template: list
) -> None:
    mocked_time.date.today.return_value = datetime.date(2032, 2, 2)
    assert outdated_products(product_template) == ["duck"]


@mock.patch("app.main.datetime")
def test_all_products_outdated(
    mocked_time: mock.Mock, product_template: list
) -> None:
    mocked_time.date.today.return_value = datetime.date(2033, 2, 2)
    assert outdated_products(product_template) == ["salmon", "chicken", "duck"]


@mock.patch("app.main.datetime")
def test_no_products_outdated(
    mocked_time: mock.Mock, product_template: list
) -> None:
    mocked_time.date.today.return_value = datetime.date(2032, 1, 1)
    assert outdated_products(product_template) == []
