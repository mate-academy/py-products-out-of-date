from unittest.mock import patch
import datetime
from app.main import outdated_products


@patch("app.main.datetime")
def test_outdated_products(mock_datetime: int) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 15)
    mock_datetime.date.side_effect = datetime.date

    products = [
        {"name": "salmon",
         "expiration_date": datetime.date(2022, 2, 10), "price": 600},
        {"name": "chicken",
         "expiration_date": datetime.date(2022, 2, 20), "price": 120},
        {"name": "duck",
         "expiration_date": datetime.date(2022, 2, 1), "price": 160}
    ]

    result = outdated_products(products)
    assert result == ["salmon", "duck"]
