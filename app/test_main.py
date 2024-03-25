from unittest.mock import patch, Mock
import datetime
import pytest

from app.main import outdated_products

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


@pytest.fixture()
def mocked_datetime() -> Mock:
    with patch("app.main.datetime") as mock_date:
        yield mock_date


def test_outdated_products_yesterday(mocked_datetime: Mock) -> None:
    mocked_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products) == ["duck"]
