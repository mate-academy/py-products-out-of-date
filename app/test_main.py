import datetime
from unittest import mock
import pytest
from app.main import outdated_products


@mock.patch("app.main.datetime")
@pytest.fixture()
def product_list() -> list:
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


def test_of_date(product_list: object, mocked_function: mock) -> None:
    mocked_function.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(product_list) == ["duck"]
