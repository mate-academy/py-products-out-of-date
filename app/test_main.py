from unittest import mock
import pytest
import datetime
from typing import Any

from app.main import outdated_products


@pytest.fixture()
def products() -> Any:
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
def test_if_products_is_outdated(mock_datetime: Any, products: list) -> Any:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    mock_datetime.date.side_effect = \
        lambda *args, **kwargs: datetime.date(*args, **kwargs)
    assert outdated_products(products) == ["duck"]
