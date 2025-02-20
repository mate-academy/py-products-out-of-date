from unittest import mock

import pytest

import datetime

from app.main import outdated_products

from typing import Any


@pytest.fixture()
def list_of_products_template() -> list:
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


@pytest.mark.parametrize(
    "list_of_products, date_to_check, expected_result",
    [
        ("list_of_products_template",
         datetime.date(2027, 2, 2),
         ["salmon", "chicken", "duck"]),
        ("list_of_products_template",
         datetime.date(2022, 2, 2),
         ["duck"]),
        ("list_of_products_template",
         datetime.date(2020, 2, 2),
         [])
    ]
)
@mock.patch("app.main.datetime")
def test_correct_date(
        mock_date: mock.MagicMock,
        list_of_products: list,
        date_to_check: datetime.date,
        expected_result: list,
        request: Any,
) -> None:
    mock_date.date.today.return_value = date_to_check
    assert (outdated_products(request.getfixturevalue(list_of_products))
            == expected_result)
