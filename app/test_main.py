import datetime
from unittest import mock
from app.main import outdated_products


def test_outdated_products() -> None:
    products = [
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
    test_date = datetime.date(2022, 2, 2)
    with mock.patch("app.main.datetime") as mock_date:
        mock_date.date.today.return_value = test_date
        assert outdated_products(products) == ["duck"]
