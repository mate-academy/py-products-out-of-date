import pytest
from unittest import mock

import datetime

from typing import Callable, List, Any

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


@pytest.mark.parametrize("date, expected_list", [
    pytest.param(
        datetime.date(2022, 2, 2),
        ["duck"],
        id="should return list with one out of date product"
    ),
    pytest.param(
        datetime.date(2022, 2, 8),
        ["chicken", "duck"],
        id="test should return list with two out of date product"
    ),
    pytest.param(
        datetime.date(2022, 2, 11),
        ["salmon", "chicken", "duck"],
        id="test should return list with tree or more out of date product"
    )
])
def test_should_return_list_of_date_product(
        date: Any,
        expected_list: list,
        products: List[dict],
        mock_datetime: Callable
) -> None:
    mock_datetime.date.today.return_value = date
    assert outdated_products(products) == expected_list


@ pytest.fixture()
def mock_datetime() -> None:
    with mock.patch("app.main.datetime") as mock_test_datetime:
        yield mock_test_datetime


def test_func_datetime_date_today_was_called(
        products: List[dict],
        mock_datetime: Callable
) -> None:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    outdated_products(products)
    mock_datetime.date.today.assert_called()


def test_raises_type_error_if_not_products() -> None:
    with pytest.raises(TypeError):
        outdated_products()
