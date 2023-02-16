import pytest
import datetime

from app.main import outdated_products


@pytest.mark.parametrize(
    "products, result", [
        ([{
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        }], ["salmon"]),
        ([{
            "name": "salmon",
            "expiration_date": datetime.date(2024, 2, 10),
            "price": 600
        }], []),
        ([{
            "name": "salmon",
            "expiration_date": datetime.date(2023, 2, 16),
            "price": 600
        }], []),
        ([{
            "name": "salmon",
            "expiration_date": datetime.date(2023, 2, 15),
            "price": 600
        }], ["salmon"]),

    ])
def test_outdated_products(products: list[dict], result: list[str]) -> None:
    assert outdated_products(products) == result
