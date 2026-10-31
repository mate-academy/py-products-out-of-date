import datetime
from unittest import mock

import pytest

from app import main


PRODUCTS = [
    {
        "name": "salmon",
        "expiration_date": datetime.date(2022, 2, 10),
        "price": 600,
    },
    {
        "name": "chicken",
        "expiration_date": datetime.date(2022, 2, 5),
        "price": 120,
    },
    {
        "name": "duck",
        "expiration_date": datetime.date(2022, 2, 1),
        "price": 160,
    },
]


@pytest.mark.parametrize(
    "today,expected",
    [
        (datetime.date(2022, 2, 2), ["duck"]),
        (datetime.date(2022, 2, 1), []),
        (datetime.date(2022, 2, 5), ["duck"]),
        (datetime.date(2022, 2, 6), ["chicken", "duck"]),
        (datetime.date(2022, 2, 11), ["salmon", "chicken", "duck"]),
        (datetime.date(2022, 1, 1), []),
    ],
)
@mock.patch("app.main.datetime")
def test_outdated_products(
    mocked_datetime: mock.MagicMock,
    today: datetime.date,
    expected: list,
) -> None:
    mocked_datetime.date.today.return_value = today
    assert main.outdated_products(PRODUCTS) == expected


@mock.patch("app.main.datetime")
def test_empty_products_list(mocked_datetime: mock.MagicMock) -> None:
    mocked_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    assert main.outdated_products([]) == []
