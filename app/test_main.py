import datetime
from unittest import mock
import pytest
from app.main import outdated_products
from typing import Any


@pytest.mark.parametrize(
    "products,expected",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600,
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120,
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160,
                },
            ],
            ["duck"],
        )
    ],
)
@mock.patch("app.main.datetime.date.today")
def test_outdated_products(
    mock_today: Any,
    products: list[dict],
    expected: list[str],
) -> None:
    mock_today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products) == expected
