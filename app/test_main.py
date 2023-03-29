import datetime
from unittest.mock import patch
from app.main import outdated_products


def test_outdated_products() -> None:
    product_list = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 3, 3),
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2023, 3, 2),
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2023, 2, 1),
        }
    ]
    result = ["chicken", "duck"]

    today = datetime.date(2023, 3, 3)
    with patch("datetime.date") as mock_datetime_date:
        mock_datetime_date.today.return_value = today

        assert outdated_products(product_list) == result
