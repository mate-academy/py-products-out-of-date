import datetime
from unittest.mock import patch
from app.main import outdated_products


def test_outdated_products() -> None:
    products = [
        {
            "name": "cheese",
            "expiration_date": datetime.date(2024, 4, 10),
            "price": 100
        },
        {
            "name": "meat",
            "expiration_date": datetime.date(2024, 3, 22),
            "price": 220
        },
        {
            "name": "milk",
            "expiration_date": datetime.date(2024, 3, 23),
            "price": 35
        }
    ]

    with patch("app.main.datetime") as mock_date:
        mock_date.date.today.return_value = datetime.date(2024, 3, 23)
        assert outdated_products(products) == ["meat"]
