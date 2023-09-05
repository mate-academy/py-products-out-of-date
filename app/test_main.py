from unittest import mock
import pytest
import datetime
from typing import List
from app.main import outdated_products


@pytest.mark.parametrize(
    "products, expected_result",
    [

        (
            [
                {"name": "salmon", "expiration_date":
                    datetime.date(2022, 2, 10), "price": 600},
                {"name": "chicken", "expiration_date":
                    datetime.date(2022, 2, 2), "price": 120},
                {"name": "duck", "expiration_date":
                    datetime.date(2022, 2, 1), "price": 160},
            ],
            ["duck"],
        ),
    ]
)
def test_outdated_products(
        products: List[dict],
        expected_result: List[str],
) -> None:
    date = datetime.date(2022, 2, 2)
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = date
        assert outdated_products(products) == expected_result
