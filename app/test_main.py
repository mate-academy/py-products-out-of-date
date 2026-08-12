from app.main import outdated_products
from unittest import mock
import datetime


def tests_for_outdated_producs() -> list:
    list_product = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]
    with mock.patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
        assert outdated_products(list_product) == ["duck"]
