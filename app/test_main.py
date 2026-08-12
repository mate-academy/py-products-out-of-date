import datetime
import pytest

from unittest import mock
from app.main import outdated_products
from typing import Any


@pytest.mark.parametrize("product_list, expected_result", [
    ([
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 10, 20),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2023, 10, 21),
            "price": 120
        },
        {
            "name": "beef",
            "expiration_date": datetime.date(2023, 10, 22),
            "price": 150
        },
        {
            "name": "milk",
            "expiration_date": datetime.date(2023, 10, 23),
            "price": 60
        },
        {
            "name": "salad",
            "expiration_date": datetime.date(2023, 10, 17),
            "price": 30
        }
    ], ["salmon", "salad"])])
@mock.patch("app.main.datetime")
def test_outdated_products(mock_datetime: Any,
                           product_list: list[dict],
                           expected_result: list) -> None:
    mock_datetime.date.today.return_value = datetime.date(2023, 10, 21)
    assert outdated_products(product_list) == expected_result
