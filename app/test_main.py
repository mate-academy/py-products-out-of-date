import pytest
from unittest.mock import patch, MagicMock
from datetime import date

from app.main import outdated_products


@pytest.fixture()
def products_template() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        }
    ]


@patch("datetime.date")
def test_should_return_product_with_valid_date(
        mock_datetime: MagicMock,
        products_template: list
) -> None:
    mock_datetime.today.return_value = date(2022, 2, 2)
    assert outdated_products(products_template) == ["duck"]


@patch("datetime.date")
def test_return_empty_list_if_all_product_outdated(
        mock_datetime: MagicMock,
        products_template: list
) -> None:
    mock_datetime.today.return_value = date(2022, 1, 30)
    assert outdated_products(products_template) == []


@patch("datetime.date")
def test_should_return_product_if_outdated_today(
        mock_datetime: MagicMock,
        products_template: list
) -> None:
    mock_datetime.today.return_value = date(2022, 2, 1)
    assert outdated_products(products_template) == []
