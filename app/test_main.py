# write your code here
import pytest
import datetime

from unittest.mock import patch, MagicMock

from app.main import outdated_products


@pytest.fixture
def products_list() -> list :
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


@patch("app.main.datetime")
def test_all_within_expiration_date(
    mocked_date: MagicMock,
    products_list: list
) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 1, 31)
    assert outdated_products(products_list) == []


@patch("app.main.datetime")
def test_one_out_of_expiration_date(
    mocked_date: MagicMock,
    products_list: list
) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 2, 4)
    assert outdated_products(products_list) == ["duck"]


@patch("app.main.datetime")
def test_all_out_of_expiration_date(
    mocked_date: MagicMock,
    products_list: list
) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 2, 24)
    assert outdated_products(products_list) == ["salmon", "chicken", "duck"]
