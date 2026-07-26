from unittest.mock import MagicMock

from app.main import outdated_products
from unittest import mock
import datetime


@mock.patch("app.main.datetime")
def test_exp_date_duck(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = datetime.date(2023, 2, 2)
    products = [{"name": "duck", "expiration_date": datetime.date(2022, 2, 2)}]
    result = outdated_products(products)
    assert result == ["duck"]


@mock.patch("app.main.datetime")
def test_exp_date_salmon(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = datetime.date(2021, 2, 2)
    products = [
        {"name": "salmon",
         "expiration_date":
             datetime.date(2022, 2, 2)}
    ]
    result = outdated_products(products)
    assert result == []


@mock.patch("app.main.datetime")
def test_exp_date_chicken(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    products = [
        {"name": "chicken",
         "expiration_date":
             datetime.date(2022, 2, 2)}
    ]
    result = outdated_products(products)
    assert result == []


@mock.patch("app.main.datetime")
def test_exp_date_all(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    products = [
        {"name": "chicken", "expiration_date": datetime.date(2022, 2, 5)},
        {"name": "salmon", "expiration_date": datetime.date(2022, 2, 10)},
        {"name": "duck", "expiration_date": datetime.date(2022, 2, 1)}
    ]
    result = outdated_products(products)
    assert result == ["duck"]
