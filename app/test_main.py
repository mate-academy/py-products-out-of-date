import pytest
import datetime
from app.main import outdated_products
from unittest.mock import patch
from typing import Callable, Any


@pytest.fixture
def mock_today() -> Any:
    today_date = datetime.date(2022, 2, 2)
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = today_date
        yield today_date


@pytest.fixture
def products_list() -> None:
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
        }
    ]
    yield products


def test_outdated_products(
        products_list: list,
        mock_today: Callable
) -> None:
    assert outdated_products(products_list) == ["duck"]
