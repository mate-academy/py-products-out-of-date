import datetime

from unittest.mock import patch, MagicMock
from app.main import outdated_products


products = [
    {
        "name": "salmon",
        "expiration_date": datetime.date(2022, 2, 10),
        "price": 600
    },
    {
        "name": "chicken",
        "expiration_date": datetime.date(2022, 2, 5),
        "price": 120
    },
    {
        "name": "duck",
        "expiration_date": datetime.date(2022, 2, 1),
        "price": 160
    },
]


@patch("app.main.datetime")
def test_one_outdated_product(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products) == ["duck"]


@patch("app.main.datetime")
def test_all_outdate_products(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 3, 5)
    assert outdated_products(products) == ["salmon", "chicken", "duck"]


@patch("app.main.datetime")
def test_expiration_date_equals_today_is_not_outdated(
        mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 9)
    assert outdated_products(products) == ["chicken", "duck"]


@patch("app.main.datetime")
def test_empty_product_list(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 1)
    assert outdated_products([]) == []


@patch("app.main.datetime")
def test_no_outdated_products(mock_datetime: MagicMock) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 1, 1)
    assert outdated_products(products) == []
