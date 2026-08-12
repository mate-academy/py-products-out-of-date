import datetime
from typing import Any, Generator
from unittest import mock

import pytest

import app.main


@pytest.fixture(scope="module")
def products(
) -> Generator[list[dict[str, str | datetime.date | int]], Any, None]:
    yield [
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


@pytest.mark.parametrize("date_current, outdated_list", [
    (datetime.date(2022, 2, 11), ["salmon", "chicken", "duck"]),
    (datetime.date(2022, 2, 10), ["chicken", "duck"]),
    (datetime.date(2022, 2, 5), ["duck"]),
    (datetime.date(2022, 2, 1), []),
])
@mock.patch("app.main.datetime.date", wraps=datetime.date)
def test_returns_outdated_products(
        mock_date : mock.Mock,
        products: list,
        date_current : datetime.date,
        outdated_list: list[dict[str, str]]
) -> None:
    mock_date.today.return_value = date_current
    assert app.main.outdated_products(products) == outdated_list
