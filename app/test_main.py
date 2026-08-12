import pytest
import datetime
from app.main import outdated_products
from unittest import mock


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
def test_all_product_is_fresh(mocked_date: mock.MagicMock,
                              product_template: list) -> None:
    mocked_date.date.today.return_value = datetime.date(2028, 12, 19)
    assert outdated_products(product_template) == ["salmon", "chicken", "duck"]


@mock.patch("app.main.datetime")
def test_all_product_out_of_date(mocked_date: mock.MagicMock,
                                 product_template: list) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 2, 10)
    assert outdated_products(product_template) == ["chicken", "duck"]


@mock.patch("app.main.datetime")
def test_any_product_out_of_date_today(mocked_date: mock.MagicMock,
                                       product_template: list) -> None:
    mocked_date.date.today.return_value = datetime.date(2021, 3, 3)
    assert outdated_products(product_template) == []
