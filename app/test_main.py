import datetime
import pytest
from app.main import outdated_products
from unittest import mock


@pytest.fixture
def mocked_time() -> mock.Mock:
    with mock.patch("app.main.datetime") as mocked:
        yield mocked


@pytest.fixture(scope="function")
def products_template() -> list:
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


def test_all_products_are_outdated(
        products_template: list, mocked_time: mock.Mock
) -> None:
    mocked_time.date.today.return_value = datetime.date(2023, 2, 10)

    assert outdated_products(
        products_template
    ) == ["salmon", "chicken", "duck"]


def test_product_is_not_outdated_with_expiration_date_equals_today(
        products_template: list, mocked_time: mock.Mock
) -> None:
    mocked_time.date.today.return_value = datetime.date(2022, 2, 5)

    assert outdated_products(products_template) == ["duck"]


def test_product_is_outdated_with_expiration_date_equals_yesterday(
        products_template: list, mocked_time: mock.Mock
) -> None:
    mocked_time.date.today.return_value = datetime.date(2022, 2, 2)

    assert outdated_products(products_template) == ["duck"]


def test_all_products_are_not_outdated(
        products_template: list, mocked_time: mock.Mock
) -> None:
    mocked_time.date.today.return_value = datetime.date(2021, 2, 10)

    assert outdated_products(products_template) == []
