import datetime
from typing import List, Dict
from unittest.mock import patch
from app.main import outdated_products


def test_outdated_products_on_specific_date() -> None:
    products: List[Dict[str, object]] = [
        {"name": "salmon", "expiration_date": datetime.date(2022, 2, 10),
         "price": 600},
        {"name": "chicken", "expiration_date": datetime.date(2022, 2, 5),
         "price": 120},
        {"name": "duck", "expiration_date": datetime.date(2022, 2, 1),
         "price": 160}
    ]

    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
        mock_datetime.date.side_effect = lambda *args, **kwargs: \
            datetime.date(*args, **kwargs)

        result = outdated_products(products)
        assert result == ["duck"]


def test_all_products_outdated() -> None:
    products: List[Dict[str, object]] = [
        {"name": "apple", "expiration_date": datetime.date(2022, 1, 1),
         "price": 50},
        {"name": "banana", "expiration_date": datetime.date(2022, 1, 15),
         "price": 30},
    ]

    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 1)
        mock_datetime.date.side_effect = lambda *args, **kwargs: \
            datetime.date(*args, **kwargs)

        result = outdated_products(products)
        assert result == ["apple", "banana"]


def test_no_outdated_products() -> None:
    products: List[Dict[str, object]] = [
        {"name": "lettuce", "expiration_date": datetime.date(2022, 3, 1),
         "price": 20},
        {"name": "broccoli", "expiration_date": datetime.date(2022, 2, 5),
         "price": 25},
    ]

    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 1)
        mock_datetime.date.side_effect = lambda *args, **kwargs: \
            datetime.date(*args, **kwargs)

        result = outdated_products(products)
        assert result == []
