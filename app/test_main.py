import datetime
from app.main import outdated_products


def test_outdated_products_in_different_cases() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 9, 25),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2023, 9, 26),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2023, 9, 29),
            "price": 160
        }
    ]
    assert outdated_products(products) == ["salmon"]
