import datetime
from typing import Any
from unittest import mock

from app.main import outdated_products


@mock.patch("app.main.datetime")
def test_outdated_products(mock_datetime_today: Any) -> None:
    mock_datetime_today.date.today.return_value = datetime.date(2022, 2, 2)

    data_if_outdated_products = [
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
    assert outdated_products(data_if_outdated_products) == ["duck"]
