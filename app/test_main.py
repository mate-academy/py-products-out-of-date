from unittest import mock
import datetime
from app.main import outdated_products


def test_mock_datetime() -> None:
    today_date = datetime.date(2022, 2, 2)
    product_list = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]
    with mock.patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = today_date
        assert outdated_products(product_list) == ["duck"]
