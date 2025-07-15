from app.main import outdated_products
import datetime
from unittest import mock


def test_expiration_day_yesterday_outdated() -> None:
    mocked_today = datetime.date(2022, 2, 2)

    products = [
        {
            "name": "apple",
            "expiration_date": datetime.date(2022, 2, 1),  # вчора
            "price": 100
        },
        {
            "name": "banana",
            "expiration_date": datetime.date(2022, 2, 2),  # сьогодні
            "price": 90
        }
    ]

    class CustomDate(datetime.date):
        @classmethod
        def today(cls) -> "CustomDate":
            return mocked_today

    with mock.patch("app.main.datetime.date", CustomDate):
        result = outdated_products(products)
        assert result == ["apple"]
