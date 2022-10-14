from app.main import outdated_products
import datetime
from unittest import mock

import pytest


@pytest.fixture()
def mock_date_time() -> None:
    with mock.patch("app.main.datetime") as mocked_date:
        yield mocked_date


@pytest.fixture()
def all_products() -> list:
    all_products = [ {
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
    yield all_products


def test_outdated_products(mock_date_time: str, all_products: list) -> None:
    mock_date_time.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(all_products) == ["duck"]
