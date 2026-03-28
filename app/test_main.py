import datetime
from unittest.mock import patch
from app.main import outdated_products


def test_product_expires_today() -> None:
    products = [
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 160
        }
    ]
    with patch("app.main.datetime") as mock_dt:
        mock_dt.date.today.return_value = datetime.date(2022, 2, 2)
        result = outdated_products(products)
    assert result == []


def test_expiration_yesterday() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 600
        },
    ]
    with patch("app.main.datetime") as mock_dt:
        mock_dt.date.today.return_value = datetime.date(2022, 2, 2)
        result = outdated_products(products)
    assert result == ["salmon"]


def test_expiration_tomorrow() -> None:
    products = [
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
    ]
    with patch("app.main.datetime") as mock_dt:
        mock_dt.date.today.return_value = datetime.date(2022, 2, 2)
        result = outdated_products(products)
    assert result == []


def test_empty_list() -> None:
    products = []
    with patch("app.main.datetime") as mock_dt:
        mock_dt.date.today.return_value = datetime.date(2022, 2, 2)
        result = outdated_products(products)
    assert result == []
