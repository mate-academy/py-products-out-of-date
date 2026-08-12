import datetime
from datetime import date
from unittest import mock
from app.main import outdated_products
from typing import Any


@mock.patch("app.main.datetime.date", wraps=datetime.date)
def test_some_date_output_but_some_date_good(mock_date: Any) -> None:
    mock_date.today.return_value = date(2026, 2, 2)
    products = [
        {
            "name": "salmon",
            "expiration_date": date(2026, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2027, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        }
    ]
    assert outdated_products(products) == ["duck"]


@mock.patch("app.main.datetime.date", wraps=datetime.date)
def test_all_date_output(mock_date: Any) -> None:
    mock_date.today.return_value = date(2026, 2, 2)
    products = [
        {
            "name": "salmon",
            "expiration_date": date(2026, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2027, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2028, 2, 1),
            "price": 160
        }
    ]
    assert outdated_products(products) == []


@mock.patch("app.main.datetime.date", wraps=datetime.date)
def test_all_date_good(mock_date: Any) -> None:
    mock_date.today.return_value = date(2026, 2, 2)
    products = [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        }
    ]
    assert outdated_products(products) == ["salmon", "chicken", "duck"]


@mock.patch("app.main.datetime.date", wraps=datetime.date)
def test_for_empty_products(mock_date: Any) -> None:
    mock_date.today.return_value = date(2026, 2, 2)
    products = []
    assert outdated_products(products) == []


@mock.patch("app.main.datetime.date", wraps=datetime.date)
def test_for_cut_off_date(mock_date: Any) -> None:
    mock_date.today.return_value = date(2026, 2, 2)
    products = [
        {
            "name": "salmon",
            "expiration_date": date(2026, 2, 2),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2026, 2, 1),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        }
    ]
    assert outdated_products(products) == ["chicken", "duck"]
