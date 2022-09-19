from datetime import date
from unittest import mock
import pytest

from app.main import outdated_products


@pytest.fixture
def products_template():
    return [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        }
    ]


@pytest.fixture
def mocked_datetime():
    with mock.patch("datetime.date") as mocked_date:
        yield mocked_date


def test_should_return_list(products_template, mocked_datetime):
    mocked_datetime.today.return_value = date(2022, 2, 6)

    result = outdated_products(products_template)

    assert isinstance(result, list)


def test_should_return_1_outdated_product(products_template, mocked_datetime):
    mocked_datetime.today.return_value = date(2022, 2, 4)

    assert outdated_products(products_template) == ["duck"]


def test_should_ignore_product_with_exp_date_same_as_today(
        products_template,
        mocked_datetime
):
    mocked_datetime.today.return_value = date(2022, 2, 10)

    assert outdated_products(products_template) == ["chicken", "duck"]


def test_should_return_product_with_exp_date_yesterday(
        products_template,
        mocked_datetime
):
    mocked_datetime.today.return_value = date(2022, 2, 6)

    assert outdated_products(products_template) == ["chicken", "duck"]
