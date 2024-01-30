# app/test_main.py
import datetime
from app.main import outdated_products
from typing import List, Dict
import pytest
from unittest.mock import patch


@pytest.mark.parametrize("input_products, expected_result", [
    (
        [
            {"name": "salmon", "expiration_date": datetime.date(2022, 2, 10), "price": 600}, # Noqa E501
            {"name": "chicken", "expiration_date": datetime.date(2022, 2, 5), "price": 120}, # Noqa E501
            {"name": "duck", "price": 160}
        ],
        ["duck"]
    ),
    # Add more test cases as needed
])
def test_outdated_products_no_expiration_date(input_products: List[Dict[str, any]], expected_result: List[str]) -> None: # Noqa E501
    mock_datetime = datetime.date(2022, 2, 2)

    with patch("app.main.datetime") as mock_datetime_obj:
        mock_datetime_obj.date.today.return_value = mock_datetime

        result: List[str] = outdated_products(input_products)
        assert result == expected_result
