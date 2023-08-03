import datetime
from app.main import outdated_products


products = [
    {
        "name": "salmon",
        "expiration_date": datetime.date(2022, 2, 10),
        "price": 600
    },
    {
        "name": "chicken",
        "expiration_date": datetime.date(2023, 8, 2),
        "price": 120
    },
    {
        "name": "duck",
        "expiration_date": datetime.date(2023, 8, 3),
        "price": 160
    }
]


def test_outdated_products() -> bool:
    result = outdated_products(products)
    assert result == ["salmon", "chicken"]
