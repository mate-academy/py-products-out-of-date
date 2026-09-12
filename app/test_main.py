import pytest
from unittest.mock import patch
from datetime import date
from app.main import outdated_products


@patch("datetime.date")
def test_outdated_products_empty_list(mock_today: pytest.Mock) -> None:
    mock_today.today.return_value = date(2022, 2, 15)
    results = outdated_products([])
    assert results == []


@patch("datetime.date")
def test_outdated_products_none_outdated(mock_today: pytest.Mock) -> None:
    mock_today.today.return_value = date(2022, 2, 1)
    products = [
        {"name": "salmon", "expiration_date": date(2022, 2, 10), "price": 600},
        {"name": "chicken", "expiration_date": date(2022, 2, 5), "price": 120},
    ]
    results = outdated_products(products)
    assert results == []


@patch("datetime.date")
def test_outdated_products_all_outdated(mock_today: pytest.Mock) -> None:
    mock_today.today.return_value = date(2022, 2, 15)
    products = [
        {"name": "salmon", "expiration_date": date(2022, 2, 10), "price": 600},
        {"name": "chicken", "expiration_date": date(2022, 2, 5), "price": 120},
    ]
    results = outdated_products(products)
    assert results == ["salmon", "chicken"]


@patch("datetime.date")
def test_outdated_products_mixed(mock_today: pytest.Mock) -> None:
    mock_today.today.return_value = date(2022, 2, 10)
    products = [
        {"name": "salmon", "expiration_date": date(2022, 2, 15), "price": 600},
        {"name": "chicken", "expiration_date": date(2022, 2, 5), "price": 120},
        {"name": "duck", "expiration_date": date(2022, 2, 1), "price": 160},
    ]
    results = outdated_products(products)
    assert results == ["chicken", "duck"]


@patch("datetime.date")
def test_outdated_products_same_day(mock_today: pytest.Mock) -> None:
    mock_today.today.return_value = date(2022, 2, 10)
    products = [
        {"name": "salmon", "expiration_date": date(2022, 2, 10), "price": 600},
    ]
    results = outdated_products(products)
    assert results == []
