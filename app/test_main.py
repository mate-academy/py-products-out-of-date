from unittest.mock import patch
import datetime
from app.main import outdated_products

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


def test_product_expired() -> None:
    from datetime import date

    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = date(2022, 10, 8)
        mock_date.side_effect = lambda *args, **kw: date(*args, **kw)
        assert outdated_products(products) == ["salmon", "chicken", "duck"]


def test_product_not_expired() -> None:
    from datetime import date

    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = date(2012, 10, 8)
        mock_date.side_effect = lambda *args, **kw: date(*args, **kw)
        assert outdated_products(products) == []


def test_product_expiration_day_today_not_outdated() -> None:
    from datetime import date

    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = date(2022, 2, 10)
        mock_date.side_effect = lambda *args, **kw: date(*args, **kw)
        assert outdated_products(products) == ["chicken", "duck"]


def test_product_expiration_day_yesterday_is_outdated() -> None:
    from datetime import date

    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = date(2022, 2, 11)
        mock_date.side_effect = lambda *args, **kw: date(*args, **kw)
        assert outdated_products(products) == ["salmon", "chicken", "duck"]
