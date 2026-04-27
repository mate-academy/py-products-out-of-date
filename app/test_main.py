import datetime
from unittest.mock import patch, MagicMock

import app.main as main


@patch("app.main.datetime")
def test_product_is_expired(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = datetime.date(2025, 1, 1)
    assert main.outdated_products([{
        "name": "salmon",
        "expiration_date": datetime.date(2022, 2, 10),
        "price": 600
    },
        {
        "name": "chicken",
        "expiration_date": datetime.date(2022, 2, 5),
        "price": 120
    }]) == ["salmon", "chicken"]


@patch("app.main.datetime")
def test_all_products_not_expired(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = datetime.date(2077, 3, 5)
    assert main.outdated_products([{
        "name": "salmon",
        "expiration_date": datetime.date(2088, 2, 10),
        "price": 600
    },
        {
        "name": "chicken",
        "expiration_date": datetime.date(2099, 2, 5),
        "price": 120
    }]) == []


@patch("app.main.datetime")
def test_half_products_expired(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = datetime.date(2026, 4, 7)
    assert main.outdated_products([{
        "name": "salmon",
        "expiration_date": datetime.date(2027, 2, 10),
        "price": 600
    },
        {
        "name": "chicken",
        "expiration_date": datetime.date(2022, 2, 5),
        "price": 120
    }]) == ["chicken"]


@patch("app.main.datetime")
def test_products_expired_today(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = datetime.date(2025, 5, 16)
    assert main.outdated_products([{
        "name": "salmon",
        "expiration_date": datetime.date(2025, 5, 16),
        "price": 600
    },
        {
        "name": "chicken",
        "expiration_date": datetime.date(2025, 5, 16),
        "price": 120
    }]) == []


@patch("app.main.datetime")
def test_products_expired_yesterday(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = datetime.date(2025, 5, 17)
    assert main.outdated_products([{
        "name": "salmon",
        "expiration_date": datetime.date(2025, 5, 16),
        "price": 600
    },
        {
        "name": "chicken",
        "expiration_date": datetime.date(2025, 5, 16),
        "price": 120
    }]) == ["salmon", "chicken"]
