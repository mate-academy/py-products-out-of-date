import datetime
from unittest.mock import patch
from app.main import outdated_products
from typing import Any


@patch("app.main.datetime")
def test_outdated_products(mock_datetime: Any) -> None:

    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)

    products_1 = [
        {"name": "salmon",
         "expiration_date": datetime.date(2022, 2, 10),
         "price": 600},
        {"name": "chicken",
         "expiration_date": datetime.date(2022, 4, 1),
         "price": 120},
        {"name": "duck",
         "expiration_date": datetime.date(2022, 5, 1),
         "price": 160},
    ]
    assert outdated_products(products_1) == []

    products_2 = [
        {"name": "salmon",
         "expiration_date": datetime.date(2022, 1, 10),
         "price": 600},
        {"name": "chicken",
         "expiration_date": datetime.date(2021, 2, 5),
         "price": 120},
        {"name": "duck",
         "expiration_date": datetime.date(1780, 2, 1),
         "price": 160},
    ]
    assert outdated_products(products_2) == ["salmon", "chicken", "duck"]

    products_3 = [
        {"name": "salmon",
         "expiration_date": datetime.date(2022, 2, 1),
         "price": 600},
        {"name": "chicken",
         "expiration_date": datetime.date(2022, 2, 5),
         "price": 120},
        {"name": "duck",
         "expiration_date": datetime.date(2022, 2, 1),
         "price": 160},
    ]
    assert outdated_products(products_3) == ["salmon", "duck"]
