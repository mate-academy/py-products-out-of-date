from datetime import date
from app.main import outdated_products
from unittest import mock
from typing import Any


@mock.patch("app.main.datetime")
def test_should_return_outdated(mocked_datetime: Any) -> None:
    mocked_datetime.date.today.return_value = date(2022, 2, 2)
    assert outdated_products([
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        }]) == ["duck"]
