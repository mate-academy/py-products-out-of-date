from datetime import date

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "products, expected_outdated",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": date(2024, 3, 5),
                    "price": 600},
                {
                    "name": "chicken", "expiration_date": date(2024, 3, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": date(2024, 3, 5),
                    "price": 160
                },
            ],
            []
        ),
        (
            [
                {
                    "name": "salmo",
                    "expiration_date": date(2024, 3, 4),
                    "price": 600},
                {
                    "name": "chicke", "expiration_date": date(2024, 3, 4),
                    "price": 120
                },
                {
                    "name": "duc",
                    "expiration_date": date(2024, 3, 4),
                    "price": 160
                },
            ],
            []
        ),
        (
            [
                {
                    "name": "beef",
                    "expiration_date": date(2024, 3, 3),
                    "price": 500
                },
                {
                    "name": "pork",
                    "expiration_date": date(2024, 3, 3),
                    "price": 150
                },
            ],
            ["beef", "pork"]
        ),
    ]
)
def test_outdated_products(
        products: list,
        expected_outdated: list
) -> None:
    assert outdated_products(products) == expected_outdated
