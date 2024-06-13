import datetime
from unittest import mock
from app.main import outdated_products


@mock.patch("datetime.date")
def test_outdated_products_before_today(mock_time_today: any) -> None:
    mock_time_today.today.return_value = datetime.datetime(2020, 1, 1)
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.datetime(2020, 10, 12),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.datetime(2020, 12, 10),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.datetime(2020, 11, 15),
            "price": 160
        }
    ]

    assert outdated_products(products) == []


@mock.patch("datetime.date")
def test_outdated_products_after_today(mock_time_today: any) -> None:
    mock_time_today.today.return_value = datetime.datetime(2020, 12, 12)
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.datetime(2020, 10, 12),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.datetime(2020, 12, 10),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.datetime(2020, 11, 15),
            "price": 160
        }
    ]

    assert outdated_products(products) == ["salmon", "chicken", "duck"]


@mock.patch("datetime.date")
def test_outdated_products_today(mock_time_today: any) -> None:
    mock_time_today.today.return_value = datetime.datetime(2020, 10, 10)
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.datetime(2020, 10, 12),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.datetime(2020, 10, 10),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.datetime(2020, 8, 15),
            "price": 160
        }
    ]

    assert outdated_products(products) == ["duck"]


@mock.patch("datetime.date")
def test_outdated_yesterday(mock_time_today: any) -> None:
    mock_time_today.today.return_value = datetime.datetime(2020, 5, 5)
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.datetime(2020, 5, 4),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.datetime(2020, 10, 10),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.datetime(2020, 5, 3),
            "price": 160
        }
    ]

    assert outdated_products(products) == ["salmon", "duck"]
