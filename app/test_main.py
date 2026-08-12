from typing import Any
import datetime
import pytest

from unittest.mock import patch, Mock
from app.main import outdated_products


@pytest.mark.parametrize(
    "current_date, input_products, expected_output",
    [
        pytest.param(
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 600,
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 120,
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160,
                },
            ],
            ["salmon", "chicken", "duck"],
            id="all the products out of expiration date",
        ),
        pytest.param(
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 600,
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 120,
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160,
                },
            ],
            ["duck"],
            id="only one product out expiration date"
        ),
        pytest.param(
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "beef",
                    "expiration_date": datetime.date(2022, 2, 20),
                    "price": 300,
                },
                {
                    "name": "pork",
                    "expiration_date": datetime.date(2022, 2, 15),
                    "price": 180,
                },
            ],
            [],
            id="expiration date is good"
        ),
        pytest.param(
            datetime.date(2022, 2, 2),
            [],
            [],
            id="no products"
        ),
    ],
)
def test_outdated_products(
    current_date: Mock,
    input_products: list[dict[str, Any]],
    expected_output: list[str]
) -> None:
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = current_date
        assert outdated_products(input_products) == expected_output
