from app.main import outdated_products
from unittest import mock
from unittest.mock import Mock

import datetime
import pytest


@pytest.mark.parametrize(
    "product_list, result",
    [
        (
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
                    "expiration_date": datetime.date(2022, 2, 4),
                    "price": 160
                }
            ], ["duck"]
        )
    ]
)
@mock.patch(
    "app.main.datetime.date",
    Mock(today=Mock(return_value=datetime.date(2022, 2, 5)))
)
def test_outdated_products(
        product_list: list[dict],
        result: list[str]
) -> None:
    assert outdated_products(product_list) == result
