import pytest

from freezegun import freeze_time

from app.main import outdated_products, datetime


@pytest.fixture()
def products():
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


@freeze_time("2022-02-3")
def test_outdated_products_1_item(products):
    assert outdated_products(products) == ["duck"]


@freeze_time("2022-02-6")
def test_outdated_products_2_item(products):
    assert outdated_products(products) == ["chicken", "duck"]


@freeze_time("2022-02-11")
def test_outdated_products_all_items(products):
    assert outdated_products(products) == ["salmon", "chicken", "duck"]


@freeze_time("2022-01-30")
def test_outdated_products_no_outdated(products):
    assert outdated_products(products) == []


@freeze_time("2022-02-01")
def test_when_date_equal_to_date(products):
    assert outdated_products(products) == []
