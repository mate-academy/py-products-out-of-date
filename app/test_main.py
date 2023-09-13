import datetime
import pytest

from unittest import mock
from app.main import outdated_products
from typing import Any


@pytest.mark.parametrize("product_list, expected_outdated_products", [
    ([
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 9, 12),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2023, 9, 15),
            "price": 120
        },
        {
            "name": "beef",
            "expiration_date": datetime.date(2023, 9, 13),
            "price": 150
        },
        {
            "name": "milk",
            "expiration_date": datetime.date(2023, 9, 13),
            "price": 60
        },
        {
            "name": "salad",
            "expiration_date": datetime.date(2023, 9, 9),
            "price": 30
        }
    ], ["salmon", "salad"])])
@mock.patch("app.main.datetime")
def test_outdated_products(mock_date: mock.MagicMock,
                           product_list: list[dict[str, Any]],
                           expected_outdated_products: list[str]) -> None:
    mock_date.date.today.return_value = datetime.date(2023, 9, 13)

    products = outdated_products(product_list)
    assert products == expected_outdated_products
