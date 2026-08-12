import pytest
import datetime
from unittest import mock
from unittest.mock import MagicMock
from app.main import outdated_products


@pytest.fixture()
def products() -> list[dict]:
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
    return products


@mock.patch("app.main.datetime")
def test_outdated_products_2022(mock_datetime: MagicMock,
                                products: list[dict]) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products) == ["duck"]


@mock.patch("app.main.datetime")
def test_outdated_products_2024(mock_datetime: MagicMock,
                                products: list[dict]) -> None:
    mock_datetime.date.today.return_value = datetime.date(2024, 2, 2)
    assert outdated_products(products) == ["salmon", "chicken", "duck"]
