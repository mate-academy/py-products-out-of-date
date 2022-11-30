from unittest import mock
import datetime
from app.main import outdated_products


@mock.patch("datetime.date")
def test_without_products_out_date(mock_date: str) -> None:
    mock_date.today.return_value = 1
    mock_date.return_value = 2
    list_goods = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        }
    ]
    assert outdated_products(list_goods) == []


@mock.patch("datetime.date")
def test_products_with_today_date(mock_date: str) -> None:
    mock_date.today.return_value = 1
    mock_date.return_value = 1
    list_goods = [
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 120
        }
    ]
    assert outdated_products(list_goods) == []


@mock.patch("datetime.date")
def test_products_with_yesterday_date(mock_date: str) -> None:
    mock_date.today.return_value = 1
    mock_date.return_value = 0
    list_goods = [
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 120
        }
    ]
    assert outdated_products(list_goods) == ["chicken"]
