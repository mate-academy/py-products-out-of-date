from datetime import date
from unittest import mock
from unittest.mock import MagicMock
from app.main import outdated_products


@mock.patch("app.main.datetime.date")
def test_dated_equal_today_products(mocked_datetime: MagicMock) -> None:
    mocked_datetime.today.return_value = date(2022, 2, 10)
    products = [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600
        }
    ]
    assert outdated_products(products) == []


@mock.patch("app.main.datetime.date")
def test_dated_fresh_products(mocked_datetime: MagicMock) -> None:
    mocked_datetime.today.return_value = date(2022, 2, 10)
    products = [
        {
            "name": "duck",
            "expiration_date": date(2022, 3, 10),
            "price": 160
        }
    ]
    assert outdated_products(products) == []


@mock.patch("app.main.datetime.date")
def test_outdated_products(mocked_datetime: MagicMock) -> None:
    mocked_datetime.today.return_value = date(2022, 2, 10)
    products = [
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 5),
            "price": 120
        }
    ]
    assert outdated_products(products) == ["chicken"]


@mock.patch("app.main.datetime.date")
def test_empty_list_of_products(mocked_datetime: MagicMock) -> None:
    mocked_datetime.today.return_value = date(2022, 2, 10)
    products = []
    assert outdated_products(products) == []


@mock.patch("app.main.datetime.date")
def test_expiration_day_yesterday_outdated(mocked_datetime: MagicMock) -> None:
    mocked_datetime.today.return_value = date(2022, 2, 10)
    products = [
        {
            "name": "turkey",
            "expiration_date": date(2022, 2, 9),
            "price": 120
        }
    ]
    assert outdated_products(products) == ["turkey"]
