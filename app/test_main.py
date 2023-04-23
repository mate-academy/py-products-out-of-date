import datetime
from unittest import mock
from app.main import outdated_products
from typing import Any

prod = [
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


@mock.patch("app.main.datetime")
def test_outdated_products(mocked_date: Any) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(prod) == ["duck"]
