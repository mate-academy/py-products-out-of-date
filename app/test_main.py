import datetime
from unittest.mock import MagicMock, patch

import pytest

from app.main import outdated_products


@pytest.fixture
def products_list() -> list:
    return [
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
        },
        {
            "name": "milk",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 50
        }
    ]


@patch("app.main.datetime")
def test_outdated_products_mixed(
        mock_datetime: MagicMock,
        products_list: list
) -> None:
    """Test standard case with valid, outdated, and today products."""
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)

    assert outdated_products(products_list) == ["duck"]


@patch("app.main.datetime")
def test_outdated_products_all_valid(
        mock_datetime: MagicMock,
        products_list: list
) -> None:
    """Test case where all products are still valid."""
    mock_datetime.date.today.return_value = datetime.date(2022, 1, 1)

    assert outdated_products(products_list) == []


@patch("app.main.datetime")
def test_outdated_products_all_outdated(
        mock_datetime: MagicMock,
        products_list: list
) -> None:
    """Test case where all products are out of date."""
    mock_datetime.date.today.return_value = datetime.date(2023, 1, 1)

    expected = ["salmon", "chicken", "duck", "milk"]
    assert outdated_products(products_list) == expected


@patch("app.main.datetime")
def test_outdated_products_empty_list(mock_datetime: MagicMock) -> None:
    """Test edge case with an empty list."""
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)

    assert outdated_products([]) == []


@patch("app.main.datetime")
def test_outdated_products_boundary_exactly_today(
        mock_datetime: MagicMock
) -> None:
    """Test boundary condition: expiration date is exactly today."""
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)

    products = [
        {
            "name": "bread",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 30
        }
    ]
    assert outdated_products(products) == []
