from unittest import mock
import pytest
from app.main import outdated_products, datetime
from typing import Callable


@pytest.fixture
def mocked_date() -> mock:
    with mock.patch("datetime.date") as mocked_date:
        yield mocked_date


@pytest.fixture()
def datetime_now() -> datetime:
    return datetime.date(2022, 2, 2)


@pytest.fixture
def food() -> list:
    return \
        [
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 2),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 2, 1),
                "price": 160
            }
        ]


def test_expiration_day_today_not_outdated(food: list,
                                           datetime_now: Callable,
                                           mocked_date: Callable)\
        -> AssertionError:
    mocked_date.today.return_value = datetime_now
    assert outdated_products(food) == ["duck"]
