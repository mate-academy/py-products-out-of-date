import datetime
from typing import List
from freezegun import freeze_time
import pytest

from app.main import outdated_products


@pytest.fixture()
def products_list() -> List[dict]:
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


@freeze_time("2022-01-31")
def test_returns_empty_list_if_all_products_fresh(
        products_list: List[dict]) -> None:
    result = outdated_products(products_list)
    assert result == []


@freeze_time("2022-02-02")
def test_returns_correct_list_for_february_2(
        products_list: List[dict]) -> None:
    result = outdated_products(products_list)
    assert result == ["duck"]


@freeze_time("2022-02-10")
def test_returns_correct_list_for_february_10(
        products_list: List[dict]) -> None:
    result = outdated_products(products_list)
    assert result == ["chicken", "duck"]


@freeze_time("2022-02-11")
def test_returns_all_products_for_february_11(
        products_list: List[dict]) -> None:
    result = outdated_products(products_list)
    assert result == ["salmon", "chicken", "duck"]
