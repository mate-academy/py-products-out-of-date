import datetime

import pytest

from app.main import outdated_products


@pytest.fixture()
def products():
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 9, 27),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 9, 26),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }]


def test_should_return_right_list(products):
    assert outdated_products(products) == ["chicken", "duck"]
