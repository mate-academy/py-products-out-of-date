import datetime
from unittest import mock

from app.main import outdated_products

MOCKED_DATE = datetime.date(2024, 3, 14)


def test_mock_datetime_today() -> None:
    goods = [
        {
            "name": "chicken",
            "expiration_date": datetime.date(2024, 3, 13),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2024, 3, 14),
            "price": 160
        }
    ]
    with mock.patch("datetime.date") as mocked_date:
        mocked_date.today.return_value = MOCKED_DATE
        assert outdated_products(goods) == ["chicken"]
