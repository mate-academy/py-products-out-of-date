from unittest import mock

import pytest
import datetime

from app.main import outdated_products


@pytest.fixture()
def mocked_date() -> None:
    with mock.patch("app.main.datetime") as mocked_date_today:
        yield mocked_date_today


def test_product_expiration(mocked_date: None) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(
        [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 1, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 20),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 3, 15),
                "price": 160
            }
        ]
    ) == ["salmon"]
