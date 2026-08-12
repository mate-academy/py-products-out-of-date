from app.main import outdated_products
import datetime
from unittest import mock


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


def test_outdated_products_should_return_all_products():
    with mock.patch("app.main.datetime") as mocked_datetime:
        mocked_datetime.date.today.return_value = datetime.date(2023, 1, 1)
        assert outdated_products(products) == ["salmon", "chicken", "duck"]


def test_outdated_products_should_return_duck():
    with mock.patch("app.main.datetime") as mocked_datetime:
        mocked_datetime.date.today.return_value = datetime.date(2022, 2, 2)
        assert outdated_products(products) == ["duck"]


def test_outdated_products_should_return_any_products():
    with mock.patch("app.main.datetime") as mocked_datetime:
        mocked_datetime.date.today.return_value = datetime.date(2021, 1, 1)
        assert outdated_products(products) == []
