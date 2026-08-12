import datetime
import pytest
from app.main import outdated_products


@pytest.mark.parametrize(
    "products, expected", [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2024, 10, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2024, 9, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2024, 8, 1),
                    "price": 160
                }
            ],
            [
                "duck"
            ]
        ),
        (
            [
                {
                    "name": "apple",
                    "expiration_date": datetime.date(2024, 8, 7),
                    "price": 50
                },
                {
                    "name": "banana",
                    "expiration_date": datetime.date(2024, 9, 5),
                    "price": 30
                }
            ],
            [
                "apple"
            ]
        ),
        (
            [
                {
                    "name": "bread",
                    "expiration_date": datetime.date(2024, 8, 8),
                    "price": 20
                },
                {
                    "name": "milk",
                    "expiration_date": datetime.date(2024, 8, 9),
                    "price": 40
                }
            ],
            []
        )
    ]
)
def test_outdated_products(
        products: list,
        expected: list
) -> None:
    result = outdated_products(products)
    assert result == expected
