import datetime
from unittest.mock import MagicMock, patch
from app.main import outdated_products


@patch("app.main.datetime")
def test_outdated_products(mock_date: MagicMock) -> None:

    mock_date.date.today.return_value = datetime.date(2022, 2, 2)

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

    assert outdated_products(products) == ["duck"]

    empty_products = []

    assert outdated_products(empty_products) == []

    not_expired_products = [
        {
            "name": "beef",
            "expiration_date": datetime.date(2022, 2, 28),
            "price": 200
        },
        {
            "name": "pork",
            "expiration_date": datetime.date(2022, 2, 15),
            "price": 180
        }
    ]
    assert outdated_products(not_expired_products) == []

    same_day_products = [
        {
            "name": "apple",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 2
        },
        {
            "name": "banana",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 1
        }
    ]

    assert outdated_products(same_day_products) == []
