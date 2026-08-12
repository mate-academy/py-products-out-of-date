import pytest
import datetime
from unittest import mock
from app.main import outdated_products


products = [
    {
        "name": "salmon",
        "expiration_date": datetime.date(2023, 3, 10),
        "price": 600
    },
    {
        "name": "chicken",
        "expiration_date": datetime.date(2023, 4, 5),
        "price": 120
    },
    {
        "name": "duck",
        "expiration_date": datetime.date(2023, 2, 1),
        "price": 160
    }
]


@pytest.fixture()
def mocked_test() -> None:
    with mock.patch("app.main.datetime") as mock_res:
        yield mock_res


def test_returns_expired_products(mocked_test: list) -> None:
    mocked_test.date.today.return_value = datetime.date(2023, 2, 8)
    assert outdated_products(products) == ["duck"]


def test_last_expiration_data(mocked_test: list) -> None:
    mocked_test.date.today.return_value = datetime.date(2023, 2, 12)
    assert outdated_products(products) == ["duck"]


def test_with_none_expiration_data(mocked_test: list) -> None:
    mocked_test.date.today.return_value = datetime.date(2023, 2, 1)
    assert outdated_products(products) == []
