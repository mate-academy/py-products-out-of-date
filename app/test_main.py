from datetime import date
from unittest import mock


from app.main import outdated_products


def test_outdated_products() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": date(2000, 4, 25),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2000, 4, 28),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2000, 4, 26),
            "price": 160
        },
        {
            "name": "Dragon",
            "expiration_date": date(2000, 4, 27),
            "price": 10000
        }
    ]
    with mock.patch("datetime.date") as mocked_date:
        mocked_date.today.return_value = date(2000, 4, 27)
        print(mocked_date.today.return_value)
        assert outdated_products(products) == ["salmon", "duck"]
