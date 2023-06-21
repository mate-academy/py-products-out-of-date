import datetime
import pytest
from app.main import outdated_products


@pytest.mark.parametrize(
    "products,expected_products",
    [
        ([{"name": "salmon", "expiration_date": datetime.date(2023, 6, 21),
           "price": 600}], []),
        ([{"name": "chicken", "expiration_date": datetime.date(2023, 6, 22),
           "price": 120}], []),
        ([{"name": "apple", "expiration_date": datetime.date(2022, 6, 20),
           "price": 10}], ["apple"])
    ]
)
def test_outdated_products(
        products: list[dict],
        expected_products: list[str]
) -> None:
    assert outdated_products(products) == expected_products
