import datetime
from datetime import date
from unittest import mock
from app.main import outdated_products
import pytest


@pytest.fixture()
def list_template():
    yield [
        {
            "name": "salmon", ""
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


def test_list_names_one_pass(list_template):
    with mock.patch("datetime.date") as mocked_today:
        mocked_today.today.return_value = date(2022, 2, 2)
        bad_product = outdated_products(list_template)
        assert bad_product == ['duck']


def test_list_all_pass(list_template):
    with mock.patch("datetime.date") as mocked_today:
        mocked_today.today.return_value = date(2022, 1, 30)
        bad_product = outdated_products(list_template)
        assert bad_product == []


def test_list_no_pass(list_template):
    with mock.patch("datetime.date") as mocked_today:
        mocked_today.today.return_value = date(2022, 2, 28)
        bad_product = outdated_products(list_template)
        assert bad_product == ['salmon', 'chicken', 'duck']


def test_list_expiration_is_today(list_template):
    with mock.patch("datetime.date") as mocked_today:
        mocked_today.today.return_value = date(2022, 2, 10)
        bad_product = outdated_products(list_template)
        assert bad_product == ['chicken', 'duck']
