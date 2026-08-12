import datetime
import pytest
from unittest import mock

from app.main import outdated_products


@pytest.fixture()
def products_template() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2025, 6, 16),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2025, 6, 16),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2025, 6, 16),
            "price": 160
        }
    ]


def test_when_day_is_tomorrow(products_template: list) -> None:
    with mock.patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2025, 6, 17)
        assert outdated_products(products_template) ==\
               ["salmon", "chicken", "duck"]


def test_when_day_equal_day(products_template: list) -> None:
    with mock.patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2025, 6, 16)
        assert outdated_products(products_template) == []


def test_when_day_is_yesterday(products_template: list) -> None:
    print(type(products_template))
    with mock.patch("app.main.datetime") as mock_datatime:
        mock_datatime.date.today.return_value = datetime.date(2025, 6, 15)
        assert outdated_products(products_template) == []
