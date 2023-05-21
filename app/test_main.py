import pytest
import datetime
from unittest import mock
from app.main import outdated_products


@pytest.fixture()
def products() -> list:
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


def test_if_product_outdate(products: list) -> None:
    with mock.patch("app.main.datetime") as mocked_datetime:
        today = datetime.date(2022, 2, 1)
        mocked_datetime.date.today.return_value = today

        assert outdated_products(products) == []

        today = datetime.date(2022, 2, 20)
        mocked_datetime.date.today.return_value = today

        assert outdated_products(products) == ["salmon", "chicken", "duck"]

        today = datetime.date(2022, 1, 20)
        mocked_datetime.date.today.return_value = today

        assert outdated_products(products) == []

        today = datetime.date(2022, 2, 6)
        mocked_datetime.date.today.return_value = today

        assert outdated_products(products) == ["chicken", "duck"]
