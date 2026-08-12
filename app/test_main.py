import pytest
import datetime
from app.main import outdated_products


@pytest.mark.parametrize(
    ("products", "expected"),
    [
        (
            [
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2024, 10, 10),
                    "price": 200
                },
                {
                    "name": "icecream",
                    "expiration_date": datetime.date(2024, 9, 26),
                    "price": 75
                },
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2024, 10, 6),
                    "price": 800
                },
                {
                    "name": "chocolate_bar",
                    "expiration_date": datetime.date(2024, 10, 5),
                    "price": 100
                },
            ],
            [
                "icecream", "chocolate_bar"
            ]
        ),
    ]
)
def test_outdated_products(
        products: list[dict],
        expected: list[str],
) -> None:
    assert outdated_products(products) == expected
