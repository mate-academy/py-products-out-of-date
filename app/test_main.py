from unittest.mock import patch
from app.main import outdated_products
import datetime


def test_one_expired_one_not_expired() -> None:
    products = [
        {"name": "milk", "expiration_date":
            datetime.date(2022, 2, 1), "price": 20},
        {"name": "bread", "expiration_date":
            datetime.date(2022, 2, 5), "price": 5},
    ]

    real_date = datetime.date

    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = real_date(2022, 2, 3)
        mock_date.side_effect = (
            lambda *args, **kwargs: datetime.date(*args, **kwargs)
        )
        result = outdated_products(products)
    assert result == ["milk"]


def test_all_product_fresh() -> None:
    products = [
        {"name": "cheese", "expiration_date":
            datetime.date(2022, 2, 10), "price": 60},
        {"name": "salmon", "expiration_date":
            datetime.date(2022, 2, 12), "price": 600},
    ]

    real_date = datetime.date

    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = real_date(2022, 2, 5)
        mock_date.side_effect = (
            lambda *args, **kwargs: datetime.date(*args, **kwargs)
        )
        result = outdated_products(products)
    assert result == []


def test_all_products_expired() -> None:
    products = [
        {"name": "chicken", "expiration_date":
            datetime.date(2022, 2, 15), "price": 55},
        {"name": "duck", "expiration_date":
            datetime.date(2022, 2, 17), "price": 155},
    ]

    real_date = datetime.date

    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = real_date(2022, 2, 20)
        mock_date.side_effect = (
            lambda *args, **kwargs: datetime.date(*args, **kwargs)
        )
        result = outdated_products(products)
    assert result == ["chicken", "duck"]


def test_mixed_products() -> None:
    products = [
        {"name": "bread", "expiration_date":
            datetime.date(2022, 2, 10), "price": 5},
        {"name": "milk", "expiration_date":
            datetime.date(2022, 2, 12), "price": 20},
        {"name": "salmon", "expiration_date":
            datetime.date(2022, 2, 9), "price": 60},
    ]

    real_date = datetime.date

    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = real_date(2022, 2, 10)
        mock_date.side_effect = (
            lambda *args, **kwargs: datetime.date(*args, **kwargs)
        )
        result = outdated_products(products)
    assert result == ["salmon"]
