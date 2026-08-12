import datetime
from unittest import mock
from app.main import outdated_products


def test_product_is_outdated() -> None:
    products = [
        {
            "name": "fish",
            "expiration_date": datetime.date(2025, 4, 1),
            "price": 600
        }
    ]

    with mock.patch.object(datetime,
                           "date",
                           mock.Mock(
                               today=mock.Mock(
                                   return_value=datetime.date(
                                       2025, 4, 2)))):
        assert outdated_products(products) == ["fish"]


def test_some_products_from_list_are_outdated() -> None:
    products = [
        {
            "name": "fish",
            "expiration_date": datetime.date(2025, 3, 30),
            "price": 600
        },
        {
            "name": "meat",
            "expiration_date": datetime.date(2025, 3, 29),
            "price": 150
        },
        {
            "name": "potato",
            "expiration_date": datetime.date(2025, 4, 4),
            "price": 200
        }
    ]

    with mock.patch.object(datetime,
                           "date",
                           mock.Mock(
                               today=mock.Mock(
                                   return_value=datetime.date(
                                       2025, 4, 3)))):
        assert outdated_products(products) == ["fish", "meat"]


def test_all_products_are_not_outdated() -> None:
    products = [
        {
            "name": "onion",
            "expiration_date": datetime.date(2025, 4, 1),
            "price": 600
        },
        {
            "name": "meat",
            "expiration_date": datetime.date(2025, 4, 1),
            "price": 150
        }
    ]

    with mock.patch.object(datetime,
                           "date",
                           mock.Mock(
                               today=mock.Mock(
                                   return_value=datetime.date(
                                       2025, 4, 1)))):
        assert outdated_products(products) == []


def test_products_list_is_empty() -> None:
    products = []

    with mock.patch.object(datetime,
                           "date",
                           mock.Mock(
                               today=mock.Mock(
                                   return_value=datetime.date(
                                       2025, 5, 12)))):
        assert outdated_products(products) == []
