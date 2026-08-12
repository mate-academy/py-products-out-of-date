from unittest import mock
from app.main import outdated_products
import datetime
import pytest


@pytest.fixture()
def product_template() -> list:
    return [
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


@mock.patch("app.main.datetime")
def test_product_outdated(mocked_date: mock,
                          product_template: list
                          ) -> None:
    mocked_date.date.today.return_value = datetime.date(2021, 2, 1)
    assert outdated_products(product_template) == []
    mocked_date.date.today.return_value = datetime.date(2022, 2, 6)
    assert outdated_products(product_template) == ["chicken", "duck"]
    mocked_date.date.today.return_value = datetime.date(2023, 4, 5)
    assert outdated_products(product_template) == ["salmon", "chicken", "duck"]
