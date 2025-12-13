import datetime
from unittest.mock import patch

from app.main import outdated_products


def test_one_outdated_product() -> None:
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
        mock_date.side_effect = (
            lambda *args, **kwargs: datetime.date(*args, **kwargs)
        )

        result = outdated_products(products)

    assert result == ["duck"]


def test_expiration_date_equal_today_not_outdated() -> None:
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
        mock_date.side_effect = (
            lambda *args, **kwargs: datetime.date(*args, **kwargs)
        )

        result = outdated_products(products)

    assert result == []


def test_all_products_outdated() -> None:
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
        mock_date.side_effect = (
            lambda *args, **kwargs: datetime.date(*args, **kwargs)
        )

        result = outdated_products(products)

    assert result == ["milk", "bread"]


def test_no_outdated_products() -> None:
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
        mock_date.side_effect = (
            lambda *args, **kwargs: datetime.date(*args, **kwargs)
        )

        result = outdated_products(products)

    assert result == []
