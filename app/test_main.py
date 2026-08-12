import pytest
import datetime
from unittest.mock import patch, MagicMock
from app.main import outdated_products


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


@patch("app.main.datetime")
def test_outdated_products(mock_date: MagicMock, product_list: list) -> None:
    mock_date.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(product_list) == ["duck"]
