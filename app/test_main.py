import pytest


from datetime import date
from typing import Any
from unittest import mock


from app.main import outdated_products


@pytest.fixture()
def mocked_datetime() -> None:
    with mock.patch("datetime.date") as mocked_datetime:
        yield mocked_datetime


@pytest.fixture()
def product_temp() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": date(2023, 2, 12),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 11, 3),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        }
    ]


@pytest.mark.parametrize(
    "today_date, result",
    [
        pytest.param(
            date(2020, 5, 19),
            [],
            id="should return no product when expiration"
               " date's of all product has not expiried"
        ),
        pytest.param(
            date(2022, 12, 4),
            ["chicken", "duck"],
            id="should return products if its date has "
               "been expiried"
        ),
        pytest.param(
            date(2022, 11, 4),
            ["chicken", "duck"],
            id="should return product if expiration "
               "date is yesterday"
        ),
        pytest.param(
            date(2022, 11, 3),
            ["duck"],
            id="should no return product if expiration "
               "date is today"
        )
    ]
)
def test_with_different_today(
        mocked_datetime: Any,
        product_temp: list,
        today_date: date,
        result: list
) -> None:
    mocked_datetime.today.return_value = today_date
    assert outdated_products(product_temp) == result
