import datetime
from unittest.mock import patch

from app.main import outdated_products


@patch("datetime.date.today")
def test_outdated_products_one_expired(mock_today) -> None:
    mock_today.return_value = datetime.date(2022, 2, 15)

    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120,
        },
    ]

    result = outdated_products(products)
    assert result == ["salmon", "chicken"]


@patch("datetime.date.today")
def test_outdated_products_all_valid(mock_today) -> None:
    mock_today.return_value = datetime.date(2022, 1, 1)

    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600,
        },
    ]

    result = outdated_products(products)
    assert result == []


@patch("datetime.date.today")
def test_outdated_products_empty_list(mock_today) -> None:
    mock_today.return_value = datetime.date(2022, 2, 15)

    result = outdated_products([])
    assert result == []
