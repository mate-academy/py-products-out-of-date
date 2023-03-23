from unittest import mock
from datetime import date
from unittest.mock import MagicMock
import pytest
from typing import Callable
from app.main import outdated_products


@pytest.fixture()
def mocked_datetime() -> Callable:
    with mock.patch("datetime.date") as mocked_time:
        yield mocked_time


def test_today_products_must_not_expired(mocked_datetime: MagicMock) -> None:
    mocked_datetime.today.return_value = date(2022, 2, 2)
    assert outdated_products([
        {
            "name": "salmon",
            "expiration_date": date(2022, 3, 23),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 2),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 1, 20),
            "price": 160
        }
    ]) == ["duck"]


def test_expiration_day_yesterday_outdated(mocked_datetime: MagicMock) -> None:
    mocked_datetime.today.return_value = date(2022, 2, 2)
    assert outdated_products([
        {
            "name": "salmon",
            "expiration_date": date(2022, 3, 23),
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
        }
    ]) == ["duck"]
