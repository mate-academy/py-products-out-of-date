from app.main import outdated_products, datetime
from unittest import mock


tested_list = [
    {"name": "valid item",
     "expiration_date": datetime.date(2020, 1, 14),
     "price": 100},
    {"name": "expired item",
     "expiration_date": datetime.date(2020, 1, 15),
     "price": 100},
]


def test_valid() -> None:
    with mock.patch("app.main.datetime") as mocked_datetime:
        today = datetime.date(2020, 1, 15)
        mocked_datetime.date.today.return_value = today
        assert outdated_products(tested_list) == ["valid item"]
