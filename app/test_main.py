from unittest import mock
import datetime
from app.main import outdated_products
import pytest


@pytest.fixture()
def mocked_datetime():
    with mock.patch("app.main.datetime") as mocked_datetime:
        yield mocked_datetime


def test_should_return_name(mocked_datetime):
    products = [
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }]
    mocked_datetime.date.today.return_value = \
        datetime.date(2022, 2, 2)

    assert outdated_products(products) == ['duck']


def test_should_return_empty_list(mocked_datetime):
    products = [
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 4),
            "price": 160
        }]
    mocked_datetime.date.today.return_value = \
        datetime.date(2022, 2, 2)

    assert outdated_products(products) == []
