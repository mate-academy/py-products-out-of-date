import datetime
from app.main import outdated_products


def test_no_outdated_products() -> None:
    products = [
        {"name": "Milk", "expiration_date": datetime.date(2022, 3, 1)},
        {"name": "Cheese", "expiration_date": datetime.date(2022, 3, 20)},
        {"name": "Bread", "expiration_date": datetime.date(2022, 3, 1)}
    ]
    assert outdated_products(products) == []
