import datetime

from unittest import mock

import pytest

from app.main import outdated_products


@pytest.fixture()
def template_list() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 3, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 3, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 3, 1),
            "price": 160
        }
    ]
    yield products


@mock.patch("app.main.datetime")
def test_outdated_products(mocked_datetime: mock, template_list: list) -> None:
    mocked_datetime.date.today.return_value = datetime.date(2022, 3, 3)
    assert outdated_products(template_list) == ["duck"]
