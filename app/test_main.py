from app.main import outdated_products
import datetime
from unittest import mock

products = [
    {
        "name": "salmon",
        "expiration_date": datetime.date.today(),
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


def test_today() -> None:
    current_day = datetime.date.today()
    with mock.patch("datetime.date") as mocked_today:

        mocked_today.today.return_value = current_day
        assert outdated_products(products) == ["chicken", "duck"]


def test_datetime_func() -> None:
    need_day = datetime.date(2022, 2, 2)
    with mock.patch("datetime.date") as mocked_func:
        mocked_func.today.return_value = need_day
        assert outdated_products(products) == ["duck"]
