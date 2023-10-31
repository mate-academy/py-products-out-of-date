import datetime
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.fixture()
def products_temp() -> list:
    return [
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
        }]


@mock.patch("app.main.datetime")
def test_check_if_all_expired(
        mocked_time: datetime,
        products_temp: list
) -> None:
    mocked_time.date.today.return_value = datetime.date(2023, 2, 3)
    assert outdated_products(products_temp) == ["salmon", "chicken", "duck"]


@mock.patch("app.main.datetime")
def test_check_if_expiration_date_equals_today(
        mocked_time: datetime,
        products_temp: list
) -> None:
    mocked_time.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products_temp) == ["duck"]
