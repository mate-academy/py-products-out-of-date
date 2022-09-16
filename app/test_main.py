# import datetime
from datetime import date
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.fixture()
def mock_datetime():
    with mock.patch("datetime.date") as mock_today:
        yield mock_today


@pytest.fixture()
def products():
    product = [
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
    return product


# @mock.patch("app.datetime.date")
def test_expiration_date_less_today_date(mock_datetime, products):
    mock_datetime.today.return_value = date(2022, 3, 10)
    assert outdated_products(products) == ["salmon",
                                           "chicken",
                                           "duck"]


def test_expiration_date_more_today_date(mock_datetime, products):
    mock_datetime.today.return_value = date(2022, 1, 10)
    assert outdated_products(products) == []


def test_expiration_date_equal_today_date(mock_datetime, products):
    mock_datetime.today.return_value = date(2022, 2, 10)
    assert outdated_products(products) == ["chicken",
                                           "duck"]


def test_list_empty(mock_datetime):
    mock_datetime.today.return_value = date(2022, 2, 10)
    assert outdated_products([]) == []


def test_raise_type_error(mock_datetime):
    mock_datetime.today.return_value = date(2022, 2, 10)
    with pytest.raises(TypeError):
        outdated_products(25)


def test_raise_key_error(mock_datetime):
    mock_datetime.today.return_value = date(2022, 2, 10)
    with pytest.raises(KeyError):
        outdated_products(
            [
                {
                    "name": "salmon",
                    "price": 600
                }
            ]
        )


def test_expiration_date_was_yesterday(mock_datetime, products):
    mock_datetime.today.return_value = date(2022, 2, 2)
    assert outdated_products(products) == ["duck"]
