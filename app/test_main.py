import pytest
from unittest import mock
from datetime import date
from typing import Any

from app.main import outdated_products


@pytest.fixture()
def products() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        }
    ]


@pytest.mark.parametrize(
    "mock_today,expected_result",
    [
        (date(2022, 1, 1), []),
        (date(2022, 2, 3), ["duck"]),
        (date(2022, 2, 5), ["duck"]),
        (date(2022, 2, 6), ["chicken", "duck"]),
        (date(2023, 6, 17), ["salmon", "chicken", "duck"])
    ],
    ids=[
        "should return empty list, as all products aren't expired",
        "should return list with `duck`, as it's expired",
        "should return list with `duck`, as it's expired",
        "should return list with `duck` and `chicken`, as they're expired",
        "should return full list, as all products are expired"
    ]
)
@mock.patch("datetime.date")
def test_should_check_outdated_products_correctly(
        mocked_date: Any,
        mock_today: Any,
        products: list[dict],
        expected_result: list[str]) -> None:
    mocked_date.today.return_value = mock_today
    assert outdated_products(products) == expected_result
