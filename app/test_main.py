from typing import List

import datetime

from unittest import mock

import pytest

from app.main import outdated_products


@pytest.fixture
def mock_today() -> List[dict]:
    original_date = datetime.date
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = original_date(2025, 1, 5)
        mock_date.side_effect = (
            lambda *args, **kwargs: original_date(*args, **kwargs)
        )
        yield mock_date


def test_outdated_products_no_expired(mock_today: List[dict]) -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2025, 1, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2025, 1, 20),
            "price": 120
        },
    ]
    assert outdated_products(products) == []


def test_outdated_products_one_expired(mock_today: List[dict]) -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2025, 1, 1),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2025, 1, 10),
            "price": 120
        },
    ]
    assert outdated_products(products) == ["salmon"]


def test_outdated_products_multiple_expired(mock_today: List[dict]) -> None:
    products = [
        {
            "name": "duck",
            "expiration_date": datetime.date(2025, 1, 1),
            "price": 160
        },
        {
            "name": "salmon",
            "expiration_date": datetime.date(2024, 12, 31),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2025, 1, 10),
            "price": 120
        },
    ]
    assert outdated_products(products) == ["duck", "salmon"]


def test_outdated_products_empty_list(mock_today: List[dict]) -> None:
    products = []
    assert outdated_products(products) == []


def test_expiration_day_today_not_outdated(mock_today: List[dict]) -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2025, 1, 5),
            "price": 600
        }
    ]
    assert outdated_products(products) == []


def test_expiration_day_yesterday_outdated(mock_today: List[dict]) -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2025, 1, 4),
            "price": 600
        }
    ]
    assert outdated_products(products) == ["salmon"]
