import datetime
from typing import Callable
from .main import outdated_products
from unittest import mock

import pytest


@pytest.fixture
def information_for_test() -> None:
    value = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date.today(),
            "price": 120
        },
        {
            "name": "pork",
            "expiration_date":
                datetime.date.today() - datetime.timedelta(days=1),
            "price": 120
        }
    ]
    return value


date_future = datetime.date(2025, 2, 5)
date_middle = datetime.date(2023, 2, 5)
date_past = datetime.date(2018, 2, 5)
today = datetime.date.today()
yesterday = datetime.date.today() - datetime.timedelta(days=1)


@mock.patch("app.main.datetime.date")
def test_some_today_is_2025_year(
        mocked_today: Callable,
        information_for_test: Callable
) -> None:

    mocked_today.today.return_value = date_future

    result = outdated_products(information_for_test)
    mocked_today.today.assert_called_with()

    assert result == ["salmon", "chicken", "pork"]


@mock.patch("app.main.datetime.date")
def test_today_is_past_est_correct(
        mocked_today: Callable,
        information_for_test: Callable
) -> None:
    mocked_today.today.return_value = date_past

    result = outdated_products(information_for_test)
    mocked_today.today.assert_called_with()

    assert result == []


@mock.patch("app.main.datetime.date")
def test_a_middle_of_estimate_date(
        mocked_today: Callable,
        information_for_test: Callable
) -> None:
    mocked_today.today.return_value = date_middle

    result = outdated_products(information_for_test)
    mocked_today.today.assert_called_with()

    assert result == ["salmon"]


@mock.patch("app.main.datetime.date")
def test_some_today(
        mocked_today: Callable,
        information_for_test: Callable
) -> None:

    mocked_today.today.return_value = today

    result = outdated_products(information_for_test)
    mocked_today.today.assert_called_with()

    assert result == ["salmon", "pork"]


@mock.patch("app.main.datetime.date")
def test_some_yesterday(
        mocked_today: Callable,
        information_for_test: Callable
) -> None:

    mocked_today.today.return_value = yesterday

    result = outdated_products(information_for_test)
    mocked_today.today.assert_called_with()

    assert result == ["salmon"]
