from app.main import outdated_products
from unittest import mock
import pytest
import datetime


@pytest.fixture()
def mocked_today_date() -> None:
    with mock.patch("app.main.datetime") as mocked_date:
        yield mocked_date


@pytest.fixture()
def products_template() -> list:
    products_template = [
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
    yield products_template


def test_should_return_expired_products(
        mocked_today_date: str,
        products_template: list
) -> None:
    mocked_today_date.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products_template) == ["duck"]
