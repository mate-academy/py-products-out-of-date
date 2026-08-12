import datetime
import pytest
from unittest import mock
from app.main import outdated_products


@pytest.fixture()
def product_list() -> None:
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
    yield products


@mock.patch("app.main.datetime")
def test_duck_is_out_of_date(mocked_date: mock, product_list: object) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(product_list) == ["duck"]


@mock.patch("app.main.datetime")
def test_chicken_and_duck__are_out_of_date(
        mocked_date: mock,
        product_list: object
) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 2, 6)
    assert outdated_products(product_list) == ["chicken", "duck"]


@mock.patch("app.main.datetime")
def test_all_products_are_out_of_date(
        mocked_date: mock,
        product_list: object
) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 2, 11)
    assert outdated_products(product_list) == \
           ["salmon", "chicken", "duck"]
