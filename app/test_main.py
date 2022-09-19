from freezegun import freeze_time
from datetime import date

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


@freeze_time("2022-02-06")
def test_should_return_list(products_template):
    result = outdated_products(products_template)

    assert isinstance(result, list)


@freeze_time("2022-02-04")
def test_should_return_one_outdated_product(products_template):
    assert outdated_products(products_template) == ["duck"]


@freeze_time("2022-02-10")
def test_should_ignore_product_with_exp_date_same_as_today(
        products_template
):
    assert outdated_products(products_template) == ["chicken", "duck"]


@freeze_time("2022-02-6")
def test_should_return_product_with_exp_date_yesterday(
        products_template
):
    assert outdated_products(products_template) == ["chicken", "duck"]
