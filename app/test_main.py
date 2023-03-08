from unittest import mock
import pytest
import datetime
from app.main import outdated_products


@pytest.fixture
def mocked_date() -> datetime:
    with mock.patch("app.main.datetime") as mocked_datetime:
        yield mocked_datetime


def test_outdated_products(mocked_date: mock) -> None:
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
    mocked_date.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products) == ["duck"]
