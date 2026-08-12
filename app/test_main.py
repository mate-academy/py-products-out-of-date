from unittest import mock
import pytest
import datetime

from app.main import outdated_products


@pytest.fixture()
def product_list():
    products_list = [
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
    yield products_list


@mock.patch("app.main.datetime")
def test_outdated_products_today(mock_datetime, product_list):
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(product_list) == ["duck"]


@mock.patch("app.main.datetime")
def test_outdated_products_yesterday(mock_datetime, product_list):
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 1)
    assert outdated_products(product_list) == []
