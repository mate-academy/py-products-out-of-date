import datetime
from unittest.mock import patch

from app.main import outdated_products


def _mock_today(fake_today: datetime.date):
    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = fake_today
        mock_date.side_effect = lambda *args, **kwargs: datetime.date(*args, **kwargs)
        yield


def test_one_outdated_product():
    fake_today = datetime.date(2022, 2, 2)

    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600,
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160,
        },
    ]

    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = fake_today
        mock_date.side_effect = lambda *args, **kwargs: datetime.date(*args, **kwargs)

        assert outdated_products(products) == ["duck"]


def test_expiration_date_equal_today_not_outdated():
    fake_today = datetime.date(2022, 2, 2)

    products = [
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 120,
        }
    ]

    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = fake_today
        mock_date.side_effect = lambda *args, **kwargs: datetime.date(*args, **kwargs)

        assert outdated_products(products) == []


def test_all_products_outdated():
    fake_today = datetime.date(2022, 2, 10)

    products = [
        {
            "name": "milk",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 40,
        },
        {
            "name": "bread",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 20,
        },
    ]

    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = fake_today
        mock_date.side_effect = lambda *args, **kwargs: datetime.date(*args, **kwargs)

        assert outdated_products(products) == ["milk", "bread"]


def test_no_outdated_products():
    fake_today = datetime.date(2022, 2, 1)

    products = [
        {
            "name": "apple",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 10,
        },
        {
            "name": "banana",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 15,
        },
    ]

    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = fake_today
        mock_date.side_effect = lambda *args, **kwargs: datetime.date(*args, **kwargs)

        assert outdated_products(products) == []

