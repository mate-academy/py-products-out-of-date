import datetime
import pytest
from unittest import mock
from app.main import outdated_products


@pytest.fixture()
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


@mock.patch("app.main.datetime")
def test_duck_is_out_of_date(
        mocked_date: mock,
        product_list: callable
) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(product_list) == ["duck"]


@mock.patch("app.main.datetime")
def test_all_products_are_out_of_date(
        mocked_date: mock,
        product_list: callable
) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 2, 11)
    assert outdated_products(product_list) == ["salmon", "chicken", "duck"]


def test_should_return_empty_list() -> None:
    assert outdated_products([]) == []


def test_returned_value_type_is_list() -> None:
    assert isinstance(outdated_products([]), list)
