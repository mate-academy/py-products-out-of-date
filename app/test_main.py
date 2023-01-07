from app.main import outdated_products
from unittest import mock

import datetime


@mock.patch("app.main.datetime")
def test_outdated_products(mocked_datetime: mock) -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]
    mocked_datetime.date.today.return_value = datetime.date(2022, 2, 3)
    assert outdated_products(products) == ["duck"]
