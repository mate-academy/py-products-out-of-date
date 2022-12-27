import datetime
import pytest

from unittest import mock
from app.main import outdated_products


@pytest.fixture
def product_list() -> None:
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
        mocked_datetime: mock.MagicMock,
        product_list: list
) -> None:
    mocked_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(product_list) == ["duck"]
