# app/test_main.py
from unittest.mock import patch
import datetime
from app.main import outdated_products
from typing import List, Dict


@patch("app.main.datetime")
def test_outdated_products_today(mock_datetime: any) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)

    products: List[Dict[str, any]] = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]

    result: List[str] = outdated_products(products)
    assert result == ["duck"]


@patch("app.main.datetime")
def test_outdated_products_future(mock_datetime: any) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 1, 1)

    products: List[Dict[str, any]] = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]

    result: List[str] = outdated_products(products)
    assert result == []


@patch("app.main.datetime")
def test_outdated_products_empty_list(mock_datetime: any) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)

    products: List[Dict[str, any]] = []

    result: List[str] = outdated_products(products)
    assert result == []


@patch("app.main.datetime")
def test_outdated_products_no_expiration_date(mock_datetime: any) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)

    products: List[Dict[str, any]] = [
        {
            "name": "salmon",
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]

    result: List[str] = outdated_products(products)
    assert result == ["duck"]
