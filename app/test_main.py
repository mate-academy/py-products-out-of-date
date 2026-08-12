from datetime import date
from unittest import mock

from app.main import outdated_products


def test_outdated_product_if_suitable_products() -> None:
    product = [
        {
            "name": "duck",
            "expiration_date": date(2023, 2, 5),
            "price": 600
        }
    ]
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = date(2023, 2, 2)

        assert outdated_products(product) == []


def test_outdated_product_if_date_today() -> None:
    product = [
        {
            "name": "duck",
            "expiration_date": date(2023, 2, 2),
            "price": 600
        }
    ]
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = date(2023, 2, 2)

        assert outdated_products(product) == []


def test_outdated_product_if_date_yesterday() -> None:
    product = [
        {
            "name": "duck",
            "expiration_date": date(2023, 2, 1),
            "price": 600
        }
    ]
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = date(2023, 2, 2)

        assert outdated_products(product) == ["duck"]
