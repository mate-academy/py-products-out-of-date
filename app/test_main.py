import datetime
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.fixture()
def products() -> list[dict]:
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


@mock.patch("app.main.datetime")
def test_correct_function(
        mocked_date_today: mock,
        products: list[dict]
) -> None:
    mocked_date_today.date.today.return_value = datetime.date(2022, 2, 2)
    outdated_products(products)
    assert products == ["duck"]
