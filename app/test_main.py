import datetime
from unittest.mock import patch
from app.main import outdated_products


@patch("app.main.datetime")
def test_outdated_products(mock_today: datetime) -> None:
    mock_today.date.today.return_value = datetime.date(2025, 1, 2)

    products = [
        {"name": "Milk", "expiration_date": datetime.date(2024, 12, 31)},
        {"name": "Eggs", "expiration_date": datetime.date(2025, 1, 5)},
        {"name": "Cheese", "expiration_date": datetime.date(2025, 1, 1)},
    ]

    expected_result = ["Milk", "Cheese"]
    result = outdated_products(products)

    assert result == expected_result
