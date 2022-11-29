import datetime
from app.main import outdated_products


def test_with_duck_out_date() -> None:
    list_goods = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 11, 30),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 12, 1),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 11, 29),
            "price": 160
        }
    ]
    assert outdated_products(list_goods) == ["duck"]
