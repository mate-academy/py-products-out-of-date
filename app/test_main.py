from unittest import mock
from unittest.mock import Mock

import pytest
import datetime

from app.main import outdated_products


@pytest.mark.parametrize(
    "list_of_products,"
    "result",
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
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ],
            ["duck"]
        ),
    ]
)
@mock.patch(
    "app.main.datetime.date",
    Mock(today=Mock(return_value=datetime.date(2022, 2, 2))))
def test_outdated_products(
        list_of_products: list[dict],
        result: list[str]
) -> None:
    assert outdated_products(list_of_products) == result
