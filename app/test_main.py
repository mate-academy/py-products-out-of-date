from datetime import date
from unittest.mock import MagicMock, patch

from app.main import outdated_products


@patch("app.main.datetime")
def test_outdated_products_some_expired(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = date(2022, 2, 2)
    products = [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 5),
            "price": 120,
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160,
        },
    ]

    assert outdated_products(products) == ["duck"]


@patch("app.main.datetime")
def test_outdated_products_none_expired(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = date(2022, 1, 1)
    products = [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 5),
            "price": 120,
        },
    ]

    assert outdated_products(products) == []


@patch("app.main.datetime")
def test_outdated_products_all_expired(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = date(2022, 3, 1)
    products = [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 5),
            "price": 120,
        },
    ]

    assert outdated_products(products) == ["salmon", "chicken"]


@patch("app.main.datetime")
def test_outdated_products_boundary_today_not_expired(
    mock_datetime: MagicMock,
) -> None:
    # Продукт з датою == сьогодні НЕ вважається простроченим
    mock_datetime.date.today.return_value = date(2022, 2, 10)
    products = [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600,
        },
    ]

    assert outdated_products(products) == []


@patch("app.main.datetime")
def test_outdated_products_empty_list(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = date(2022, 2, 2)

    assert outdated_products([]) == []
