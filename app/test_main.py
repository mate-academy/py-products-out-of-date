import datetime

from unittest.mock import MagicMock

from app.main import outdated_products


def test_good_products() -> None:
    datetime_mock = MagicMock(wrap=datetime.datetime)
    datetime_mock.now.return_value = datetime.datetime(2022, 10, 14)
    assert outdated_products([{
        "name": "salmon",
        "expiration_date": datetime.date(2022, 10, 30),
        "price": 600
    }, {
        "name": "chicken",
        "expiration_date": datetime.date(2022, 11, 5),
        "price": 120
    }, {
        "name": "duck",
        "expiration_date": datetime.date(2022, 12, 10),
        "price": 160
    }]) == []


def test_all_outdated_products() -> None:
    datetime_mock = MagicMock(wrap=datetime.datetime)
    datetime_mock.now.return_value = datetime.datetime(2022, 10, 14)
    assert outdated_products([{
        "name": "salmon",
        "expiration_date": datetime.date(2022, 3, 30),
        "price": 600
    }, {
        "name": "chicken",
        "expiration_date": datetime.date(2022, 5, 5),
        "price": 120
    }, {
        "name": "duck",
        "expiration_date": datetime.date(2021, 12, 10),
        "price": 160
    }]) == ["salmon", "chicken", "duck"]


def test_one_day_outdated_products() -> None:
    datetime_mock = MagicMock(wrap=datetime.datetime)
    datetime_mock.now.return_value = datetime.datetime(2022, 10, 14)
    assert outdated_products([{
        "name": "salmon",
        "expiration_date": datetime.date(2022, 10, 13),
        "price": 600
    }]) == ["salmon"]


def test_today_okay_products() -> None:
    datetime_mock = MagicMock(wrap=datetime.datetime)
    datetime_mock.now.return_value = datetime.datetime(2022, 10, 14)
    assert outdated_products([{
        "name": "salmon",
        "expiration_date": datetime.date(2022, 10, 14),
        "price": 600
    }]) == []
