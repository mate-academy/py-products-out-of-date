import datetime
from unittest.mock import patch
from app.main import outdated_products


def test_outdated_products_with_expired_products() -> None:
    mock_today = datetime.date(2022, 2, 2)
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = mock_today

        products = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 1, 30),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 1, 31),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 2, 3),
                "price": 160
            }
        ]
        assert outdated_products(products) == ["salmon", "chicken"]


def test_outdated_products_with_no_expired_products() -> None:
    mock_today = datetime.date(2022, 2, 2)
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = mock_today

        products = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 5),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 8),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 2, 10),
                "price": 160
            }
        ]
        assert outdated_products(products) == []
