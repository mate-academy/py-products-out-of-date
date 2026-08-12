from __future__ import annotations
import pytest
from datetime import date
from unittest import mock
from unittest.mock import MagicMock, AsyncMock
from typing import Generator
from app.main import outdated_products


@pytest.fixture
def products_list() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": date(2025, 11, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2025, 11, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2025, 11, 1),
            "price": 160
        }
    ]


@pytest.fixture
def mock_datetime() -> Generator[MagicMock | AsyncMock]:
    with mock.patch(
        "app.main.datetime.date"
    ) as mocked_datetime:
        yield mocked_datetime


def test_all_products_outdated(
        products_list: list,
        mock_datetime: MagicMock | AsyncMock
) -> None:
    mock_datetime.today.return_value = date(2025, 11, 20)
    assert outdated_products(products_list) == ["salmon", "chicken", "duck"]


def test_none_products_outdated(
        products_list: list,
        mock_datetime: MagicMock | AsyncMock
) -> None:
    mock_datetime.today.return_value = date(2025, 10, 20)
    assert outdated_products(products_list) == []


def test_some_products_outdated(
        products_list: list,
        mock_datetime: MagicMock | AsyncMock
) -> None:
    mock_datetime.today.return_value = date(2025, 11, 5)
    assert outdated_products(products_list) == ["duck"]


def test_product_outdated_one_day(
        products_list: list,
        mock_datetime: MagicMock | AsyncMock
) -> None:
    mock_datetime.today.return_value = date(2025, 11, 6)
    assert outdated_products(products_list) == ["chicken", "duck"]
