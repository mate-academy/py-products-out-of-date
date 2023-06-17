import datetime

import pytest

from app.main import outdated_products

from unittest import mock

from typing import Any


@pytest.fixture
def test_mock_datetime() -> Any:
    with mock.patch("app.main.datetime") as mocked_datetime:
        yield mocked_datetime


@pytest.fixture
def test_fixture() -> list:
    products = [
    {
     "name": "salmon",
     "expiration_date": datetime.date(2023, 6, 25),
     "price": 600
    },
    {
     "name": "chicken",
     "expiration_date": datetime.date(2023, 6, 17),
     "price": 120
    },
    {
     "name": "duck",
     "expiration_date": datetime.date(2023, 6, 16),
     "price": 160
    }
    ]
    return products


def test_outdated_products_is_duck(
 test_fixture: list,
 test_mock_datetime: Any
) -> None:
    test_mock_datetime.date.today.return_value = datetime.date(2023, 6, 17)
    assert outdated_products(test_fixture) == ["duck"]
