import datetime

import pytest

from typing import Callable
from unittest import mock

from app.main import outdated_products


dict_products = [
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

@pytest.fixture()
def mocked_func() -> None:
    with mock.patch("datetime.date.today") as mocked_today:
        yield mocked_today


@pytest.mark.parametrize(
    "cur_date,result",
    [
        (datetime.date(2022, 2, 5), ["duck"]),
        (datetime.date(2022, 2, 2), ["duck"]),
        (datetime.date(2021, 2, 3), []),
    ]
)
def test_outdated_products(cur_date: datetime.date, result: list):
    class NewDate(datetime.date):
        @classmethod
        def today(cls):
            return cur_date

    datetime.date = NewDate

    assert outdated_products(dict_products) == result

