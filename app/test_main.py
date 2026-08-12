import pytest
import datetime

from app.main import outdated_products


@pytest.mark.parametrize(
    "products,result",
    [(
        [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2026, 1, 28),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2026, 1, 27),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2026, 1, 26),
                "price": 160
            }
        ],
        ["duck"]
    )]
)
def test_outdated_products(products: list[dict], result: list) -> None:
    assert outdated_products(products) == result
