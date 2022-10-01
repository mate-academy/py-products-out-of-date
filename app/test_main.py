import pytest
from datetime import date
from unittest import mock

from app.main import outdated_products


@pytest.fixture()
def product_template():
    return [
        {
            "name": "salmon",
            "expiration_date": date(2022, 10, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 10, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 10, 2),
            "price": 160
        }
    ]


@pytest.mark.parametrize(
    "check_date, out_products",
    [
        pytest.param(
            date(2022, 10, 12),
            ["salmon", "chicken", "duck"],
            id="Should return all products"
        ),
        pytest.param(
            date(2022, 10, 7),
            ["chicken", "duck"],
            id="Should return only outdated product"
        ),
        pytest.param(
            date(2022, 10, 5),
            ["duck"],
            id=("Should return product with expiration "
                "date equals yesterday is outdated")
        ),
        pytest.param(
            date(2022, 10, 3),
            ["duck"],
            id="Should return empty list if no outdated prod"
        )
    ]
)
@mock.patch("app.main.datetime.date")
def test_outdated_products(mocked_datetime,
                           product_template,
                           check_date,
                           out_products):
    mocked_datetime.today.return_value = check_date
    assert outdated_products(product_template) == out_products
