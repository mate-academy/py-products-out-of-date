import datetime
from unittest import mock

from app.main import outdated_products


def test_returns_list_of_names() -> None:
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
    mocked_today = datetime.date(2022, 2, 6)
    with mock.patch("datetime.date") as mocked_date_today:
        mocked_date_today.today.return_value = mocked_today
        assert outdated_products(products) == ["chicken", "duck"]


def test_expiration_day_today_not_outdated() -> None:
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
    mocked_today = datetime.date(2022, 2, 1)
    with mock.patch("datetime.date") as mocked_date_today:
        mocked_date_today.today.return_value = mocked_today
        assert outdated_products(products) == []
