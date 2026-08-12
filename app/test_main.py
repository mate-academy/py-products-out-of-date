import pytest

from unittest import mock
from app.main import datetime, outdated_products


@pytest.mark.parametrize(
    "products, expected_result",
    [
        pytest.param(
            [
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
            ],
            [
                "duck"
            ]
        )
    ]
)
@mock.patch("app.main.datetime")
def test_should_return_name_product_if_actual_date(
        mocked_datetime,
        products,
        expected_result
):
    mocked_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products) == expected_result
