import datetime
from unittest import mock

from .main import outdated_products

FAKE_TODAY_DATE = datetime.date(2022, 2, 2)

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
    },
    {
        "name": "eggs",
        "expiration_date": datetime.date(2022, 2, 2),
        "price": 70
    }
]


@mock.patch("datetime.date")
def test_expired_data(datetime_mock: mock) -> None:
    datetime_mock.today.return_value = FAKE_TODAY_DATE
    assert outdated_products(products) == ["duck"]
