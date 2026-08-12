# write your code here
from unittest import mock
import datetime

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "product, expected",
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
            ["duck"],
            id="test outdated product"
        )
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_product(mock_datetime: datetime,
                          product: list,
                          expected: list) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(product) == expected
