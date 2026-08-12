import pytest

import datetime

from unittest import mock

from app.main import outdated_products


@pytest.mark.parametrize(
    "today_fake_date, products, outdated_product",
    [
        (
            datetime.date(2022, 2, 2),
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
            ["duck"]
        )
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(mocked_date,
                           today_fake_date,
                           products,
                           outdated_product):
    mocked_date.date.today.return_value = today_fake_date
    assert outdated_products(products) == outdated_product
