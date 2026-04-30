
from unittest import mock
from datetime import datetime

from app.main import outdated_products


def test_outdated_products() -> None:
    products = [
        {"name": "Milk", "expiration_date": datetime(2023, 1, 1).date()},
        {"name": "Bread", "expiration_date": datetime(2024, 1, 1).date()},
        {"name": "Cheese", "expiration_date": datetime(2022, 12, 31).date()},
    ]

    with mock.patch('app.main.datetime') as mock_datetime:
        mock_datetime.date.today.return_value = datetime(2023, 1, 1).date()
        result = outdated_products(products)

    assert result == ["Cheese"]
