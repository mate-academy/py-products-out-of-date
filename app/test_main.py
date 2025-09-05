import pytest
from unittest.mock import patch, MagicMock
from datetime import date
from app.main import outdated_products


@pytest.fixture
def products_list() -> list[dict]:
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
        },
        {
            "name": "milk",
            "expiration_date": date(2022, 2, 2),
            "price": 30
        }
    ]


@patch("app.main.datetime.date")
def test_outdated_products_found(
    mock_date: MagicMock, products_list: list[dict]
) -> None:
    mock_date.today.return_value = date(2022, 2, 6)
    expected_result = ["duck", "milk", "chicken"]
    result = outdated_products(products_list)
    assert sorted(result) == sorted(expected_result)


@patch("app.main.datetime.date")
def test_no_outdated_products(
    mock_date: MagicMock, products_list: list[dict]
) -> None:
    mock_date.today.return_value = date(2022, 1, 31)
    expected_result = []
    result = outdated_products(products_list)
    assert result == expected_result


@patch("app.main.datetime.date")
def test_all_products_outdated(
    mock_date: MagicMock, products_list: list[dict]
) -> None:
    mock_date.today.return_value = date(2022, 2, 11)
    expected_result = ["salmon", "chicken", "duck", "milk"]
    result = outdated_products(products_list)
    assert sorted(result) == sorted(expected_result)


@patch("app.main.datetime.date")
def test_expiration_date_is_today(
    mock_date: MagicMock, products_list: list[dict]
) -> None:
    mock_date.today.return_value = date(2022, 2, 5)
    expected_result = ["duck", "milk"]
    result = outdated_products(products_list)
    assert sorted(result) == sorted(expected_result)
