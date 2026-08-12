import datetime
from unittest.mock import patch
from app.main import outdated_products


def test_no_outdated_products() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 12, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2023, 12, 15),
            "price": 120
        }
    ]
    with patch("app.main.get_today_date",
               return_value=datetime.date(2023, 12, 1)):
        assert outdated_products(products) == [], (
            "Expected no outdated products"
        )


def test_some_outdated_products() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 11, 15),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2023, 12, 1),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2023, 11, 30),
            "price": 160
        }
    ]
    with patch("app.main.get_today_date",
               return_value=datetime.date(2023, 12, 1)):
        assert outdated_products(products) == ["salmon", "duck"], (
            "Expected 'salmon' and 'duck' to be outdated"
        )


def test_all_outdated_products() -> None:
    products = [
        {
            "name": "beef",
            "expiration_date": datetime.date(2023, 11, 20),
            "price": 800
        },
        {
            "name": "pork",
            "expiration_date": datetime.date(2023, 11, 25),
            "price": 550
        }
    ]
    with patch("app.main.get_today_date",
               return_value=datetime.date(2023, 12, 1)):
        assert outdated_products(products) == ["beef", "pork"], (
            "Expected all products to be outdated"
        )


def test_empty_products_list() -> None:
    products = []
    with patch("app.main.get_today_date",
               return_value=datetime.date(2023, 12, 1)):
        assert outdated_products(products) == [], (
            "Expected no products in an empty list"
        )
