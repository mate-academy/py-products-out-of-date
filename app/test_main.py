import datetime
from unittest.mock import patch

from app.main import outdated_products


class MockDate(datetime.date):
    @classmethod
    def today(cls) -> datetime.date:
        return datetime.date(2022, 1, 10)


def test_data_today() -> None:
    with patch("app.main.datetime.date", MockDate):
        value = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 1, 15),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 1, 13),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 1, 8),
                "price": 160
            }
        ]
        assert outdated_products(value) == ["duck"]


def test_data_today_expire() -> None:
    with patch("app.main.datetime.date", MockDate):
        value = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 1, 15),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 1, 13),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 1, 10),
                "price": 160
            }
        ]
        assert outdated_products(value) == []


def test_data_expired() -> None:
    with patch("app.main.datetime.date", MockDate):
        value = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 1, 15),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 1, 9),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 1, 10),
                "price": 160
            }
        ]
        assert outdated_products(value) == ["chicken"]
