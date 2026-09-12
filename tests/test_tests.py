from datetime import date
from unittest.mock import patch
from app.main import outdated_products


def test_expiration_day_today_not_outdated() -> None:
    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = date(2022, 2, 2)
        products = [
            {"name": "salmon", "expiration_date":
             date(2022, 2, 2), "price": 600}
        ]
        assert outdated_products(products) == []


def test_expiration_day_yesterday_outdated() -> None:
    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = date(2022, 2, 2)
        products = [
            {"name": "duck", "expiration_date": date(2022, 2, 1), "price": 160}
        ]
        assert outdated_products(products) == ["duck"]
