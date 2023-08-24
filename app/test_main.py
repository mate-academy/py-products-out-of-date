import datetime
from typing import Callable, Any
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.fixture
def test_products() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 9, 30),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120,
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2023, 9, 30),
            "price": 160,
        },
    ]


@pytest.fixture
def mocked_datetime() -> Any:
    with mock.patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2023, 7, 30)
        yield mock_datetime


def test_check_for_outdated(
    test_products: list, mocked_datetime: Callable
) -> None:
    result = outdated_products(test_products)

    mocked_datetime.date.today.assert_called()
    assert "chicken" in result
    assert "duck" not in result
    assert "salmon" not in result
