import datetime
import pytest
from typing import List, Dict

from app.main import outdated_products


@pytest.mark.parametrize(
    "products, expected",
    [
        (
            [
                {
                    "name": "bread",
                    "expiration_date": datetime.date(2025, 4, 30),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2025, 5, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2025, 5, 1),
                    "price": 160
                }
            ],
            ["bread"],
        )
    ]
)
def test_outdated_products(products: List[Dict[str, any]],
                           expected: List[str]) -> None:
    assert outdated_products(products) == expected
