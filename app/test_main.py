import datetime
from unittest.mock import MagicMock
from unittest.mock import patch
import pytest

from app.main import outdated_products


@pytest.fixture
def list_of_products() -> list:
    return [{"name": "salmon",
             "expiration_date": datetime.date(2026, 9, 26),
             "price": 600},
            {"name": "chicken",
             "expiration_date": datetime.date(2026, 9, 25),
             "price": 120},
            {"name": "duck",
             "expiration_date": datetime.date(2026, 9, 27),
             "price": 160}]


@patch("app.main.datetime")
def test_should_return_correct_list_of_products(
    mocked_date: MagicMock,
    list_of_products: list
) -> None:
    mocked_date.date.today.return_value = datetime.date(2026, 9, 27)
    assert outdated_products(list_of_products) == ["salmon", "chicken"]
