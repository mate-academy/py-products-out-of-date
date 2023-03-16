import datetime
import pytest
from app.main import outdated_products
from freezegun import freeze_time


def mocked_time() -> datetime:
    return datetime.date.today()


@pytest.fixture
def products_template() -> list:
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


@freeze_time("2022-02-24")
def test_all_products_are_outdated(products_template: list) -> None:
    mocked_time()
    assert outdated_products(
        products_template
    ) == ["salmon", "chicken", "duck"]


@freeze_time("2022-02-05")
def test_product_is_not_outdated_with_expiration_date_equals_today(
        products_template: list
) -> None:
    mocked_time()
    assert outdated_products(products_template) == ["duck"]


@freeze_time("2022-02-02")
def test_product_is_outdated_with_expiration_date_equals_yesterday(
        products_template: list
) -> None:
    mocked_time()
    assert outdated_products(products_template) == ["duck"]


@freeze_time("2021-02-24")
def test_all_products_are_not_outdated(products_template: list) -> None:
    mocked_time()
    assert outdated_products(products_template) == []
