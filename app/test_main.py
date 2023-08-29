import datetime
from unittest import mock
import pytest
from app.main import outdated_products


@pytest.fixture()
def products_template() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 8, 28),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2023, 8, 29),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        },
        {
            "name": "beef",
            "expiration_date": datetime.date(2024, 5, 5),
            "price": 200
        }
    ]


def test_outdated_products_when_date_is_today(
        products_template: list[dict]
) -> None:

    with mock.patch("app.main.datetime") as mocked_today:
        mocked_today.date.today.return_value = datetime.date(2023, 8, 29)
        assert outdated_products(products_template) == ["salmon", "duck"]


def test_outdated_products_when_date_is_yesterday(
        products_template: list[dict]
) -> None:
    with mock.patch("app.main.datetime") as mocked_today:
        mocked_today.date.today.return_value = datetime.date(2023, 8, 28)
        assert outdated_products(products_template) == ["duck"]
