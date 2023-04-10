import datetime
import pytest
from unittest import mock
from app.main import outdated_products


@pytest.fixture()
def mock_time() -> None:
    with mock.patch("app.main.datetime") as mocked_time:
        yield mocked_time


def test_outdated_products(mock_time: mock.Mock) -> None:
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
    mock_time.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products) == ["duck"]
