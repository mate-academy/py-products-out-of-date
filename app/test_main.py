import pytest

import datetime

from unittest.mock import patch

from app.main import outdated_products

from unittest import mock


@pytest.fixture()
def mocked_date() -> datetime:
    with patch("app.main.datetime") as mocked_datetime:
        yield mocked_datetime


@patch("app.main.datetime")
def test_should_return_list_of_expired_products(
        mocked_datetime: mock.Mock
) -> None:
    products_list = [
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

    mocked_datetime.date.today.return_value = datetime.date(2022, 5, 5)
    assert outdated_products(products_list) == ["salmon", "chicken", "duck"]
