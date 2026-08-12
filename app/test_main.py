import datetime
from typing import Callable
from unittest import mock
from app.main import outdated_products


@mock.patch("app.main.datetime")
def test_outdated_products(mock_datetime: Callable) -> None:
    product_list = [
        {
            "name": "sausages",
            "expiration_date": datetime.date(2023, 2, 25),
            "price": 600
        },
        {
            "name": "milk",
            "expiration_date": datetime.date(2023, 2, 1),
            "price": 120
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2023, 2, 5),
            "price": 350
        },
        {
            "name": "meat",
            "expiration_date": datetime.date(2023, 2, 4),
            "price": 400
        }

    ]

    mock_datetime.date.today.return_value = datetime.date(2023, 2, 5)
    assert outdated_products(product_list) == ["milk", "meat"]
