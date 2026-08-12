import datetime
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.fixture()
def products() -> tuple:
    return ([
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
    ], ["duck"])


def test_outdated_products(products: tuple) -> None:
    with mock.patch("app.main.datetime") as date_time:
        date_time.date.today.return_value = datetime.date(2022, 2, 2)
        product, expected = products
        assert outdated_products(product) == expected
