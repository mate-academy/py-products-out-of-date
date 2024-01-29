import datetime
from unittest import mock
from app.main import outdated_products


def test_outdated_products() -> None:
    products = [
        {"name": "salmon",
         "expiration_date": datetime.date(2022, 2, 9),
         "price": 600},
        {"name": "chicken",
         "expiration_date": datetime.date(2022, 2, 5),
         "price": 120},
        {"name": "duck",
         "expiration_date": datetime.date(2022, 2, 7),
         "price": 160},
        {"name": "pork",
         "expiration_date": datetime.date(2022, 2, 8),
         "price": 140}
    ]
    today_date = datetime.date(2022, 2, 8)
    with mock.patch("app.main.datetime.date") as mocked_datetime:
        mocked_datetime.today.return_value = today_date
        assert outdated_products(products) == ["chicken", "duck"]
