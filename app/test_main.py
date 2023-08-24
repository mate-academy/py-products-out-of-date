import datetime

from freezegun import freeze_time
import pytest

from app.main import outdated_products


@pytest.fixture()
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


@freeze_time("2022-01-29")
def test_nothing_outdated(products_template: list) -> None:
    assert outdated_products(products_template) == []


@freeze_time("2022-02-01")
def test_when_today_is_not_outdated(products_template: list) -> None:
    assert outdated_products(products_template) == []


@freeze_time("2022-02-02")
def test_duck_is_outdated(products_template: list) -> None:
    assert outdated_products(products_template) == ["duck"]


@freeze_time("2022-03-01")
def test_everything_is_outdated(products_template: list) -> None:
    assert outdated_products(products_template) == [
        "salmon",
        "chicken",
        "duck"
    ]
