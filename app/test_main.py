import datetime
import pytest
from unittest.mock import MagicMock, patch

from app.main import outdated_products


@pytest.fixture
def product_list() -> list:
    return ([
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
    ])


@patch("app.main.datetime")
def test_outdated_one_product(
        mock_date: MagicMock,
        product_list: list
) -> None:
    mock_date.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(product_list) == ["duck"]


@patch("app.main.datetime")
def test_all_outdated_products(
        mock_date: MagicMock,
        product_list: list
) -> None:
    mock_date.date.today.return_value = datetime.date(2022, 2, 12)
    assert outdated_products(product_list) == ["salmon", "chicken", "duck"]


@patch("app.main.datetime")
def test_same_date(
        mock_date: MagicMock,
        product_list: list
) -> None:
    mock_date.date.today.return_value = datetime.date(2022, 2, 1)
    assert outdated_products(product_list) == []


@patch("app.main.datetime")
def test_with_no_outdated_products(
        mock_date: MagicMock,
        product_list: list
) -> None:
    mock_date.date.today.return_value = datetime.date(2022, 1, 30)
    assert outdated_products(product_list) == []
