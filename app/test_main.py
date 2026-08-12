from unittest import mock
from app.main import outdated_products
from datetime import date
import pytest


@pytest.fixture()
def products_template() -> list[dict]:
    return [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        }
    ]


def test_outdated_products(products_template: list) -> None:
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = date(2022, 2, 2)
        assert outdated_products(products_template) == ["duck"]


def test_expiration_day_today_not_outdated(products_template: list) -> None:
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = date(2022, 2, 1)
        assert outdated_products(products_template) == []
