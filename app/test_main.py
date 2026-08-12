import pytest
import datetime
from unittest import mock
from app.main import outdated_products


@pytest.fixture
def product_ls() -> list:
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


@mock.patch("app.main.datetime")
def test_outdated_products(
        mock_datatime: mock.MagicMock,
        product_ls: list) -> None:
    mock_datatime.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(product_ls) == ["duck"]
