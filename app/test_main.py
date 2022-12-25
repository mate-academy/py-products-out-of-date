import datetime
from typing import Any

from freezegun import freeze_time
import pytest

from app.main import outdated_products


@pytest.fixture()
def products() -> list:
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
        }
    ]


@freeze_time("2022-02-02")
def test_expiration_day_yesterday(products: list) -> Any:
    assert outdated_products(products) == ["duck"]


@freeze_time("2022-02-10")
def test_expiration_day_today_not_outdated(products: list) -> Any:
    assert outdated_products(products) == ["chicken", "duck"]
