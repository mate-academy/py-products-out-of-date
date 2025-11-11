import datetime
from unittest.mock import patch
from app.main import outdated_products


def test_single_outdated_product() -> None:
    today = datetime.date(2022, 2, 2)
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = today
        mock_datetime.date.side_effect = (
            lambda *args, **kwargs: datetime.date(*args, **kwargs)
        )
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
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 2, 1),
                "price": 160,
            },
        ]
        assert outdated_products(products) == ["duck"]


def test_all_products_outdated() -> None:
    today = datetime.date(2022, 3, 1)
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = today
        mock_datetime.date.side_effect = (
            lambda *args, **kwargs: datetime.date(*args, **kwargs)
        )
        products = [
            {
                "name": "milk",
                "expiration_date": datetime.date(2022, 2, 28),
                "price": 10,
            },
            {
                "name": "cheese",
                "expiration_date": datetime.date(2022, 1, 15),
                "price": 30,
            },
        ]
        assert outdated_products(products) == ["milk", "cheese"]


def test_no_products_outdated() -> None:
    today = datetime.date(2022, 1, 1)
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = today
        mock_datetime.date.side_effect = (
            lambda *args, **kwargs: datetime.date(*args, **kwargs)
        )
        products = [
            {
                "name": "bread",
                "expiration_date": datetime.date(2022, 1, 2),
                "price": 5,
            },
            {
                "name": "butter",
                "expiration_date": datetime.date(2022, 1, 3),
                "price": 15,
            },
        ]
        assert outdated_products(products) == []


def test_expiration_date_equals_today() -> None:
    today = datetime.date(2022, 2, 2)
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = today
        mock_datetime.date.side_effect = (
            lambda *args, **kwargs: datetime.date(*args, **kwargs)
        )
        products = [
            {
                "name": "yogurt",
                "expiration_date": datetime.date(2022, 2, 2),
                "price": 8,
            },
            {
                "name": "cream",
                "expiration_date": datetime.date(2022, 2, 1),
                "price": 12,
            },
        ]
        assert outdated_products(products) == ["cream"]


def test_empty_product_list() -> None:
    today = datetime.date(2022, 2, 2)
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = today
        mock_datetime.date.side_effect = (
            lambda *args, **kwargs: datetime.date(*args, **kwargs)
        )
        assert outdated_products([]) == []
