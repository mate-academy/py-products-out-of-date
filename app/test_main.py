import datetime
from unittest.mock import patch
from app.main import outdated_products
from typing import Any

MOCK_TODAY = datetime.date(2022, 2, 2)
_real_date = datetime.date  # сохраняем оригинальный класс datetime.date


@patch("app.main.datetime.date", autospec=True)
def test_outdated_products_with_some_expired(mock_date: Any) -> None:
    mock_date.today.return_value = MOCK_TODAY
    mock_date.side_effect = (
        lambda *args, **kwargs: _real_date(*args, **kwargs)
    )

    products = [
        {"name": "salmon", "expiration_date": datetime.date(2022, 2, 10),
         "price": 600},
        {"name": "chicken", "expiration_date": datetime.date(2022, 2, 5),
         "price": 120},
        {"name": "duck", "expiration_date": datetime.date(2022, 2, 1),
         "price": 160},
    ]
    assert outdated_products(products) == ["duck"]


@patch("app.main.datetime.date", autospec=True)
def test_outdated_products_all_expired(mock_date: Any) -> None:
    mock_date.today.return_value = MOCK_TODAY
    mock_date.side_effect = (
        lambda *args, **kwargs: _real_date(*args, **kwargs)
    )

    products = [
        {"name": "milk", "expiration_date": datetime.date(2022, 1, 30),
         "price": 50},
        {"name": "bread", "expiration_date": datetime.date(2022, 1, 1),
         "price": 20},
    ]
    assert outdated_products(products) == [
        "milk",
        "bread",
    ]


@patch("app.main.datetime.date", autospec=True)
def test_outdated_products_none_expired(mock_date: Any) -> None:
    mock_date.today.return_value = MOCK_TODAY
    mock_date.side_effect = (
        lambda *args, **kwargs: _real_date(*args, **kwargs)
    )

    products = [
        {"name": "cheese", "expiration_date": datetime.date(2022, 2, 2),
         "price": 200},
        {"name": "yogurt", "expiration_date": datetime.date(2022, 2, 3),
         "price": 80},
    ]
    assert outdated_products(products) == []


@patch("app.main.datetime.date", autospec=True)
def test_outdated_products_empty_list(mock_date: Any) -> None:
    mock_date.today.return_value = MOCK_TODAY
    mock_date.side_effect = (
        lambda *args, **kwargs: _real_date(*args, **kwargs)
    )

    assert outdated_products([]) == []
