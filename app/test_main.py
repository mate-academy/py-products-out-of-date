# write your code here
import datetime
from datetime import date
from unittest import mock
from unittest.mock import MagicMock

from app.main import outdated_products

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
        "name": "burito",
        "expiration_date": datetime.date(2023, 2, 21),
        "price": 120
    },
    {
        "name": "yoghurt",
        "expiration_date": datetime.date.today(),
        "price": 120
    },
    {
        "name": "duck",
        "expiration_date": datetime.date(2022, 2, 1),
        "price": 160
    }]


@mock.patch("app.main.datetime.date")
def test_outdated_are_spotted_ok(mock_date: MagicMock) -> None:
    mock_date.today.return_value = date(2023, 10, 8)
    assert outdated_products(products) == [x.get("name") for x in products]


@mock.patch("app.main.datetime.date")
def test_fresh_are_not_spotted_ok(mock_date: MagicMock) -> None:
    mock_date.today.return_value = date(2010, 10, 8)
    assert outdated_products(products) == []


@mock.patch("app.main.datetime.date")
def test_expiration_date_today_is_not_expired_ok(mock_date: MagicMock) -> None:
    mock_date.today.return_value = date.today()
    assert outdated_products(products) == ["salmon", "chicken",
                                           "burito", "duck"]


@mock.patch("app.main.datetime.date")
def test_expiration_date_yesterday_is_expired_ok(mock_date: MagicMock) -> None:
    mock_date.today.return_value = date.today()
    assert outdated_products(products) == ["salmon", "chicken",
                                           "burito", "duck"]
