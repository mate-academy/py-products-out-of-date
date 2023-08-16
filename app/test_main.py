import datetime
from typing import List
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.fixture()
def info() -> List[dict]:
    return [{
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


@pytest.mark.parametrize(
    "date, result",
    [
        (datetime.date(2022, 2, 11), ["salmon", "chicken", "duck"]),
        (datetime.date(2022, 2, 8), ["chicken", "duck"]),
        (datetime.date(2022, 2, 3), ["duck"]),
        (datetime.date(2022, 2, 1), [])
    ]
)
@mock.patch("datetime.date")
def test_products(
        mock_datetime: mock,
        info: List[dict],
        date: tuple,
        result: list
) -> None:
    mock_datetime.today.return_value = date
    assert outdated_products(info) == result
