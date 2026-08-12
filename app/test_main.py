from typing import Any
from unittest.mock import MagicMock
import datetime

import pytest
from unittest import mock

from app.main import outdated_products


@pytest.fixture
def mock_today() -> Any:
    with mock.patch("app.main.datetime") as mocked_datetime:
        fake_day = datetime.date(2025, 12, 23)
        mocked_datetime.date.today.return_value = fake_day
        yield mocked_datetime


def test_outdated_products(mock_today: MagicMock) -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2025, 12, 22),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2025, 12, 23),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2025, 12, 24),
            "price": 160
        },
        {
            "name": "cheese",
            "expiration_date": datetime.date(2024, 1, 1),
            "price": 160
        },
        {
            "name": "milk",
            "expiration_date": datetime.date(2026, 1, 1),
            "price": 160
        }
    ]
    assert outdated_products(products) == ["salmon", "cheese"]
