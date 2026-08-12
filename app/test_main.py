from app.main import outdated_products
import datetime
from datetime import date
from unittest.mock import patch


@patch("app.main.datetime")
def test_outdated_products(mock_datetime: datetime) -> None:
    mock_date = datetime.date(2022, 2, 2)
    mock_datetime.date.today.return_value = mock_date

    products = [
        {"name": "salmon", "expiration_date": date(2022, 2, 10), "price": 600},
        {"name": "chicken", "expiration_date": date(2022, 2, 5), "price": 120},
        {"name": "duck", "expiration_date": date(2022, 2, 1), "price": 160}
    ]
    assert outdated_products(products) == ["duck"]

    products = [
        {"name": "salmon", "expiration_date": date(2022, 2, 10), "price": 600},
        {"name": "chicken", "expiration_date": date(2022, 2, 5), "price": 120},
        {"name": "duck", "expiration_date": date(2022, 2, 15), "price": 160}
    ]
    assert outdated_products(products) == []

    products = [
        {"name": "salmon", "expiration_date": date(2022, 1, 10), "price": 600},
        {"name": "chicken", "expiration_date": date(2022, 1, 5), "price": 120},
        {"name": "duck", "expiration_date": date(2022, 1, 1), "price": 160}
    ]
    assert outdated_products(products) == ["salmon", "chicken", "duck"]
