import datetime

import pytest

from app.main import outdated_products
from typing import Callable
from unittest import mock


products_ = [
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


@pytest.fixture()
def mocked_datetime_date_today() -> None:
    with mock.patch("datetime.date") as mocked_datetime:
        yield mocked_datetime


@pytest.mark.parametrize(
    "products, date, result",
    [
        (products_, datetime.date(2022, 2, 1), []),
        (products_, datetime.date(2022, 2, 2), ["duck"]),
        (products_, datetime.date(2025, 1, 1), ["salmon", "chicken", "duck"])
    ]
)
def test_of_correct_operation(
        products: list,
        date: datetime,
        result: list,
        mocked_datetime_date_today: Callable
) -> None:
    mocked_datetime_date_today.today.return_value = date
    assert outdated_products(products) == result
