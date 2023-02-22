from unittest import mock
import pytest
import datetime

from app.main import outdated_products


@pytest.fixture()
def products() -> None:
    yield [
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


@mock.patch("app.main.datetime", wraps=datetime)
def test_no_outdated_products(mocked_today: object, products: list) -> None:
    mocked_today.date.today.return_value = datetime.date(2022, 2, 1)
    assert outdated_products(products) == []


@mock.patch("app.main.datetime", wraps=datetime)
def test_all_outdated_products(mocked_today: object, products: list) -> None:
    mocked_today.date.today.return_value = datetime.date(2022, 2, 20)
    assert outdated_products(products) == ["salmon", "chicken", "duck"]


@mock.patch("app.main.datetime", wraps=datetime)
def test_one_outdated_product(mocked_today: object, products: list) -> None:
    mocked_today.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products) == ["duck"]
