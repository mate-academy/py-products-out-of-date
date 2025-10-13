import datetime
from unittest.mock import patch
from app.main import outdated_products


def test_expiration_yesterday_is_outdated() -> None:
    products = [
        {
            "name": "milk",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 10,
        }
    ]
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
        mock_datetime.date.side_effect = (
            lambda *a, **kw: datetime.date(*a, **kw)
        )
        result = outdated_products(products)
    assert result == ["milk"]


def test_expiration_today_is_not_outdated() -> None:
    products = [
        {
            "name": "bread",
            "expiration_date": datetime.date(2022, 2, 2),
            "price": 5,
        }
    ]
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
        mock_datetime.date.side_effect = (
            lambda *a, **kw: datetime.date(*a, **kw)
        )
        result = outdated_products(products)
    assert result == []


def test_expiration_tomorrow_is_not_outdated() -> None:
    products = [
        {
            "name": "meat",
            "expiration_date": datetime.date(2022, 2, 3),
            "price": 25,
        }
    ]
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
        mock_datetime.date.side_effect = (
            lambda *a, **kw: datetime.date(*a, **kw)
        )
        result = outdated_products(products)
    assert result == []


def test_multiple_products_some_outdated() -> None:
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
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
        mock_datetime.date.side_effect = (
            lambda *a, **kw: datetime.date(*a, **kw)
        )
        result = outdated_products(products)
    assert result == ["duck"]


def test_no_products_outdated() -> None:
    products = [
        {
            "name": "apple",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 5,
        },
        {
            "name": "orange",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 6,
        },
    ]
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
        mock_datetime.date.side_effect = (
            lambda *a, **kw: datetime.date(*a, **kw)
        )
        result = outdated_products(products)
    assert result == []
