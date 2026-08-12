import datetime
from unittest.mock import patch, Mock

from app.main import outdated_products


@patch("datetime.date", Mock(wraps=datetime.date))
def test_when_there_is_no_outdated_products() -> None:
    fixed_date = datetime.date(2023, 5, 10)
    datetime.date.today.return_value = fixed_date
    product = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 5, 12),
            "price": 600
        },
        {
            "name": "eggs",
            "expiration_date": datetime.date(2023, 5, 11),
            "price": 600
        }
    ]
    assert outdated_products(product) == []


@patch("datetime.date", Mock(wraps=datetime.date))
def test_when_there_is_outdated_products() -> None:
    fixed_date = datetime.date(2023, 5, 10)
    datetime.date.today.return_value = fixed_date
    product = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 5, 9),
            "price": 600
        },
        {
            "name": "eggs",
            "expiration_date": datetime.date(2023, 5, 8),
            "price": 600
        }
    ]
    assert outdated_products(product) == ["salmon", "eggs"]


@patch("datetime.date", Mock(wraps=datetime.date))
def test_when_expiration_date_equal_to_today_day() -> None:
    fixed_date = datetime.date(2023, 5, 10)
    datetime.date.today.return_value = fixed_date
    product = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 5, 10),
            "price": 600
        },
        {
            "name": "eggs",
            "expiration_date": datetime.date(2023, 5, 10),
            "price": 600
        }
    ]
    assert outdated_products(product) == []
