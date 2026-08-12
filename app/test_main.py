from app.main import outdated_products
import datetime


def test_outdated_products() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2024, 6, 3),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2024, 6, 2),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]
    assert outdated_products(products) == ["chicken", "duck"]
