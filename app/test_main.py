from datetime import date
from unittest.mock import patch
import app.main as main


def test_some_case() -> None:
    products = [
        {"name": "duck", "expiration_date": date(2022, 2, 1), "price": 160},
        {"name": "chicken", "expiration_date": date(2022, 2, 5), "price": 120},
    ]
    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = date(2022, 2, 2)
        mock_date.side_effect = lambda *args, **kwargs: date(*args, **kwargs)
        result = main.outdated_products(products)
        assert result == ["duck"]


def test_expiration_date_equal_today_not_outdated() -> None:
    products = [
        {"name": "milk", "expiration_date": date(2022, 2, 2), "price": 50},
    ]
    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = date(2022, 2, 2)
        mock_date.side_effect = lambda *a, **kw: date(*a, **kw)
        assert main.outdated_products(products) == []
