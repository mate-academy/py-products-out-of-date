import pytest
import datetime
from typing import Callable
from unittest import mock
from app.main import outdated_products


@pytest.fixture()
def mocked_date_time_today() -> Callable:
    with mock.patch("datetime.date.today()") as mocked_today:
        yield mocked_today


def test_outdated_products(
        mocked_date_time_today: Callable
) -> None:
    mocked_date_time_today.return_value = datetime.date(2022, 2, 2)
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
    assert outdated_products(products) == ["duck"]
