import datetime
from unittest import mock
from unittest.mock import patch

from app.main import outdated_products


@patch("app.main.datetime")
def test_outdated_products(mock_datetime: mock) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)

    products = [
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
    assert outdated_products(products) == ["duck"]

    products = [
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 3),
            "price": 160
        }
    ]

    assert outdated_products(products) == []
