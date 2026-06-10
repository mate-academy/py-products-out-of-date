from unittest.mock import patch, MagicMock
from datetime import date
from app.main import outdated_products


@patch("app.main.datetime")
def test_outdated(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = date(2022, 2, 3)
    products = [
        {"name": "salmon", "expiration_date": date(2022, 2, 10), "price": 600},
        {"name": "chicken", "expiration_date": date(2022, 2, 5), "price": 120},
        {"name": "duck", "expiration_date": date(2022, 2, 1), "price": 160}
    ]
    result = outdated_products(products)
    assert result == ["duck"]


@patch("app.main.datetime")
def test_all_products_not_outdated(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = date(2022, 1, 1)
    products = [
        {"name": "salmon", "expiration_date": date(2022, 2, 10), "price": 600},
        {"name": "chicken", "expiration_date": date(2022, 2, 5), "price": 120},
        {"name": "duck", "expiration_date": date(2022, 2, 1), "price": 160}
    ]
    result = outdated_products(products)
    assert result == []


@patch("app.main.datetime")
def test_part_of_product_outdated(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = date(2022, 2, 3)
    products = [
        {"name": "salmon", "expiration_date": date(2022, 2, 10), "price": 600},
        {"name": "chicken", "expiration_date": date(2022, 2, 2), "price": 120},
        {"name": "duck", "expiration_date": date(2022, 2, 1), "price": 160}
    ]
    result = outdated_products(products)
    assert result == ["chicken", "duck"]


@patch("app.main.datetime")
def test_empty_list(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = date(2022, 2, 3)
    products = []
    result = outdated_products(products)
    assert result == []
