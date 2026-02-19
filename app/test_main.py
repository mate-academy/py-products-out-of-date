import datetime
import pytest
from app.main import outdated_products


@pytest.mark.parametrize(
    "products, expected_outdated_products",
    [
        (
            [{"name": "salmon",
              "expiration_date": datetime.date(2026, 2, 20),
              "price": 600}],
            []
        ),
        (
            [
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2026, 2, 19),
                    "price": 120
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2026, 2, 18),
                    "price": 140
                },
                {
                    "name": "pork",
                    "expiration_date": datetime.date(2025, 2, 18),
                    "price": 250
                }
            ],
            ["chicken", "pork"],
        ),
        ([], []),
    ]
)
def test_restore_names_functionality(products: list,
                                     expected_outdated_products: list) -> None:
    assert outdated_products(products) == expected_outdated_products
