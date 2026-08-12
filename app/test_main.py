import datetime
from unittest.mock import patch
import app.main


def test_returns_outdated_product() -> None:
    today = datetime.date(2022, 2, 2)
    products = [
        {"name": "duck", "expiration_date": datetime.date(2022, 2, 1),
         "price": 160},
    ]
    with patch("app.main.datetime") as mock_dt:
        mock_dt.date.today.return_value = today
        assert app.main.outdated_products(products) == ["duck"]


def test_does_not_return_fresh_product() -> None:
    today = datetime.date(2022, 2, 2)
    products = [
        {"name": "salmon", "expiration_date": datetime.date(2022, 2, 10),
         "price": 600},
    ]
    with patch("app.main.datetime") as mock_dt:
        mock_dt.date.today.return_value = today
        assert app.main.outdated_products(products) == []


def test_product_expiring_today_is_not_outdated() -> None:
    today = datetime.date(2022, 2, 2)
    products = [
        {"name": "chicken", "expiration_date": datetime.date(2022, 2, 2),
         "price": 120},
    ]
    with patch("app.main.datetime") as mock_dt:
        mock_dt.date.today.return_value = today
        assert app.main.outdated_products(products) == []


def test_returns_multiple_outdated_products() -> None:
    today = datetime.date(2022, 2, 2)
    products = [
        {"name": "salmon", "expiration_date": datetime.date(2022, 2, 10),
         "price": 600},
        {"name": "chicken", "expiration_date": datetime.date(2022, 2, 5),
         "price": 120},
        {"name": "duck", "expiration_date": datetime.date(2022, 2, 1),
         "price": 160},
        {"name": "beef", "expiration_date": datetime.date(2022, 1, 15),
         "price": 200},
    ]
    with patch("app.main.datetime") as mock_dt:
        mock_dt.date.today.return_value = today
        assert app.main.outdated_products(products) == ["duck", "beef"]


def test_returns_empty_list_when_no_products() -> None:
    today = datetime.date(2022, 2, 2)
    with patch("app.main.datetime") as mock_dt:
        mock_dt.date.today.return_value = today
        assert app.main.outdated_products([]) == []


def test_returns_empty_list_when_all_fresh() -> None:
    today = datetime.date(2022, 2, 2)
    products = [
        {"name": "salmon", "expiration_date": datetime.date(2022, 2, 10),
         "price": 600},
        {"name": "chicken", "expiration_date": datetime.date(2022, 2, 5),
         "price": 120},
    ]
    with patch("app.main.datetime") as mock_dt:
        mock_dt.date.today.return_value = today
        assert app.main.outdated_products(products) == []


def test_returns_all_when_all_outdated() -> None:
    today = datetime.date(2022, 2, 2)
    products = [
        {"name": "duck", "expiration_date": datetime.date(2022, 2, 1),
         "price": 160},
        {"name": "beef", "expiration_date": datetime.date(2022, 1, 15),
         "price": 200},
    ]
    with patch("app.main.datetime") as mock_dt:
        mock_dt.date.today.return_value = today
        assert app.main.outdated_products(products) == ["duck", "beef"]
