from app.main import outdated_products
import datetime
from unittest.mock import patch

@patch("app.main.datetime")
def test_outdated_products(mock_date):
    mock_date.date.today.return_value = datetime.date(2022, 2, 10)

    products = [
        {"name": "salmon", "expiration_date": datetime.date(2022, 2, 10), "price": 1919},
        {"name": "chicken", "expiration_date": datetime.date(2022, 2, 5), "price": 19},
        {"name": "butter", "expiration_date": datetime.date(2022, 2, 1), "price": 91}
    ]

    assert outdated_products(products) == ["chicken", "butter"]
