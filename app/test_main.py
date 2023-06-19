from datetime import date
from pytest import fixture
from unittest import mock

from app.main import outdated_products


@fixture()
def product_template() -> list:
    return [
        {
            "name": "chicken",
            "expiration_date": date(2024, 2, 10),
            "price": 600
        },
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600
        }]


def test_outdated_products(product_template: list) -> None:
    with mock.patch("datetime.date") as mocked_datetime:
        mocked_datetime.today.return_value = date(2023, 2, 10)
        assert outdated_products(product_template) == ["salmon"]

        mocked_datetime.today.return_value = date(2024, 2, 10)
        assert outdated_products(product_template) == ["salmon"]

        mocked_datetime.today.return_value = date(2024, 2, 11)
        assert outdated_products(product_template) == ["chicken", "salmon"]
