from unittest.mock import MagicMock
from unittest.mock import patch
import datetime
from app.main import outdated_products


def test_when_there_are_bad_products() -> None:
    mocked_date = MagicMock()
    mocked_date.date.today.return_value = datetime.date(2022, 2, 2)
    products = [
        {"name": "salmon",
         "expiration_date": datetime.date(2022, 2, 10),
         "price": 600},

        {"name": "chicken",
         "expiration_date": datetime.date(2022, 2, 5),
         "price": 120},

        {"name": "duck",
         "expiration_date": datetime.date(2022, 2, 1),
         "price": 160},
    ]
    with patch("app.main.datetime", mocked_date):
        result = outdated_products(products)
        assert result == ["duck"]


def test_when_all_products_are_good() -> None:
    mocked_date = MagicMock()
    mocked_date.date.today.return_value = datetime.date(2022, 2, 2)
    products = [
        {"name": "salmon",
         "expiration_date": datetime.date(2022, 2, 10),
         "price": 600},

        {"name": "chicken",
         "expiration_date": datetime.date(2022, 2, 5),
         "price": 120},

        {"name": "duck",
         "expiration_date": datetime.date(2022, 2, 3),
         "price": 160},
    ]
    with patch("app.main.datetime", mocked_date):
        result = outdated_products(products)
        assert result == []


def test_limit_test() -> None:
    mocked_date = MagicMock()
    mocked_date.date.today.return_value = datetime.date(2022, 2, 2)
    products = [
        {"name": "salmon",
         "expiration_date": datetime.date(2022, 2, 2),
         "price": 600},

        {"name": "chicken",
         "expiration_date": datetime.date(2022, 2, 1),
         "price": 120},

        {"name": "duck",
         "expiration_date": datetime.date(2022, 2, 2),
         "price": 160},
    ]
    with patch("app.main.datetime", mocked_date):
        result = outdated_products(products)
        assert result == ["chicken"]


def test_empty_list() -> None:
    mocked_date = MagicMock()
    mocked_date.date.today.return_value = datetime.date(2022, 2, 2)
    products = []
    with patch("app.main.datetime", mocked_date):
        result = outdated_products(products)
        assert result == []
