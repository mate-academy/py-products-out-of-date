import datetime
from unittest.mock import MagicMock, patch

from app.main import outdated_products

REAL_DATE = datetime.date


@patch("app.main.datetime.date")
def test_no_outdated_products(mock_date: MagicMock) -> None:
    mock_date.today.return_value = REAL_DATE(2022, 2, 2)
    mock_date.side_effect = REAL_DATE

    products = [
        {
            "name": "salmon",
            "expiration_date": REAL_DATE(2022, 2, 2),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": REAL_DATE(2022, 2, 5),
            "price": 120,
        },
    ]

    assert outdated_products(products) == []


@patch("app.main.datetime.date")
def test_one_outdated_product(mock_date: MagicMock) -> None:
    mock_date.today.return_value = REAL_DATE(2022, 2, 2)
    mock_date.side_effect = REAL_DATE

    products = [
        {
            "name": "salmon",
            "expiration_date": REAL_DATE(2022, 2, 10),
            "price": 600,
        },
        {
            "name": "duck",
            "expiration_date": REAL_DATE(2022, 2, 1),
            "price": 160,
        },
    ]

    assert outdated_products(products) == ["duck"]


@patch("app.main.datetime.date")
def test_all_outdated_products(mock_date: MagicMock) -> None:
    mock_date.today.return_value = REAL_DATE(2022, 2, 2)
    mock_date.side_effect = REAL_DATE

    products = [
        {
            "name": "milk",
            "expiration_date": REAL_DATE(2022, 1, 30),
            "price": 10,
        },
        {
            "name": "bread",
            "expiration_date": REAL_DATE(2022, 2, 1),
            "price": 8,
        },
    ]

    assert outdated_products(products) == ["milk", "bread"]


@patch("app.main.datetime.date")
def test_empty_products(mock_date: MagicMock) -> None:
    mock_date.today.return_value = REAL_DATE(2022, 2, 2)
    mock_date.side_effect = REAL_DATE

    assert outdated_products([]) == []
