import datetime
from unittest import mock
from app.main import outdated_products
import pytest


@pytest.fixture
def product_list() -> list:
    return [
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
        }
    ]


def test_outdated_products(product_list: list[dict]) -> None:
    with mock.patch("app.main.datetime") as mock_today:
        mock_today.date.today.return_value = datetime.date(2022, 2, 3)
        result = outdated_products(product_list)
        assert result == ["duck"]
