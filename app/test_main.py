from unittest.mock import patch, MagicMock
from app.main import outdated_products
import datetime
import pytest


@pytest.fixture(scope="module")
def prepare_products() -> None:
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
    return products


@pytest.fixture
def datetime_mock() -> None:
    with patch("app.main.datetime") as mock_datetime:
        yield mock_datetime


def test_outdated_products_(
    prepare_products: callable, datetime_mock: MagicMock
) -> None:
    datetime_mock.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(prepare_products) == ["duck"]
