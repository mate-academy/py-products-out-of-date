from __future__ import annotations
from unittest import mock
import pytest
import datetime
from datetime import date
from app.main import outdated_products


@pytest.fixture()
def mock_date_today() -> None:
    with mock.patch("datetime.date") as mock_today:
        yield mock_today


def test_equal_date(mock_date_today: callable) -> None:
    mock_date_today.return_value = date(2022, 2, 5)
    mock_date_today.today.return_value = date(2022, 2, 5)
    products_for_check = [
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        }
    ]
    assert outdated_products(products_for_check) == []


def test_date_future(mock_date_today: callable) -> None:
    mock_date_today.return_value = date(2022, 2, 1)
    mock_date_today.today.return_value = date(2022, 2, 2)
    products_for_check = [
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]
    assert outdated_products(products_for_check) == ["duck"]


def test_date_past(mock_date_today: callable) -> None:
    mock_date_today.return_value = date(2022, 2, 10)
    mock_date_today.today.return_value = date(2022, 2, 2)
    products_for_check = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        }
    ]
    assert outdated_products(products_for_check) == []
