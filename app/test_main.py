from typing import Callable
import pytest
from unittest import mock
from datetime import date

from app.main import outdated_products


@pytest.fixture
def mocked_date() -> Callable:
    with mock.patch("datetime.date") as mock_today:
        yield mock_today


def test_outdated_products_works(mocked_date: mock.MagicMock) -> None:
    mocked_date.today.return_value = date(2021, 2, 10)
    assert outdated_products([
        {
            "name": "salmon",
            "expiration_date": date(2021, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2021, 2, 9),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2021, 2, 10),
            "price": 160
        }
    ]) == ["chicken"]
