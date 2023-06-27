import pytest
import datetime

from unittest import mock
from typing import Any
from app.main import outdated_products


@pytest.fixture()
def products_template() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10)
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5)
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1)
        },
        {
            "name": "ice_cream",
            "expiration_date": datetime.date(2022, 1, 28)
        },
        {
            "name": "chocolate",
            "expiration_date": datetime.date(2022, 3, 10)
        }
    ]


@mock.patch("app.main.datetime")
def test_outdated_products(
        mocked_date: Any,
        products_template: list[dict]
) -> None:

    mocked_date.date.today.return_value = datetime.date(2022, 2, 2)

    outdated = outdated_products(products_template)

    assert outdated == ["duck", "ice_cream"]
