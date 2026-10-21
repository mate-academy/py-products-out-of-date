import datetime
from unittest.mock import MagicMock, patch
from app import main

real_date = datetime.date


@patch("app.main.datetime.date")
def test_outdated_products_filters_correctly(mock_date: MagicMock) -> None:
    mock_date.today.return_value = real_date(2022, 2, 2)
    mock_date.side_effect = lambda y, m, d: real_date(y, m, d)

    products = [
        {
            "name": "salmon",
            "expiration_date": real_date(2022, 2, 10),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": real_date(2022, 2, 5),
            "price": 120,
        },
        {
            "name": "duck",
            "expiration_date": real_date(2022, 2, 1),
            "price": 160,
        },
    ]

    assert main.outdated_products(products) == ["duck"]


@patch("app.main.datetime.date")
def test_product_expires_today_not_outdated(mock_date: MagicMock) -> None:
    mock_date.today.return_value = real_date(2022, 2, 2)
    mock_date.side_effect = lambda y, m, d: real_date(y, m, d)

    products = [
        {
            "name": "milk",
            "expiration_date": real_date(2022, 2, 2),
            "price": 50,
        }
    ]

    assert main.outdated_products(products) == []


@patch("app.main.datetime.date")
def test_outdated_products_empty_list(mock_date: MagicMock) -> None:
    mock_date.today.return_value = real_date(2022, 2, 2)
    assert main.outdated_products([]) == []
