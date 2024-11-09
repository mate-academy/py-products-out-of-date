from unittest.mock import patch, Mock
import datetime
from app.main import outdated_products


def test_outdated_products() -> None:
    today = datetime.date(2022, 2, 2)
    yesterday = today - datetime.timedelta(days=1)
    tomorrow = today + datetime.timedelta(days=1)

    with patch("datetime.date", Mock(today=Mock(return_value=today))):
        products = [
            {"name": "salmon", "expiration_date": tomorrow, "price": 600},
            {"name": "chicken", "expiration_date": yesterday, "price": 120},
            {"name": "duck",
             "expiration_date": today, "price": 160}  # expires today
        ]

        result = outdated_products(products)
        assert result == ["chicken"]
