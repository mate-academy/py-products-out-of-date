import datetime
import pytest
from unittest import mock

from app.main import outdated_products


@pytest.fixture()
def products_template() -> list:
    return [{"name": "cheese",
             "expiration_date": datetime.date(2022, 2, 5),
             "price": 600}]


@mock.patch("app.main.datetime")
def test_prod_exist(mocked_datetime: mock, products_template: list) -> None:
    mocked_datetime.date.today.return_value = datetime.date(2022, 1, 10)
    assert outdated_products(products_template) == []


@mock.patch("app.main.datetime")
def test_out_products(mocked_datetime: mock, products_template: list) -> None:
    mocked_datetime.date.today.return_value = datetime.date(2022, 2, 10)
    assert outdated_products(products_template) == ["cheese"]
# write your code here
