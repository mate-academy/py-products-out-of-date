import pytest

import datetime
from unittest import mock

from app.main import outdated_products


@pytest.fixture()
def products_template() -> list[dict]:
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


@pytest.mark.parametrize(
    "date,expired",
    [
        (datetime.date(2022, 1, 13), []),
        (datetime.date(2022, 3, 13), [
            "salmon", "chicken", "duck"
        ]),
        (datetime.date(2022, 2, 3), ["duck"])
    ]
)
def test_outdated_products(
        products_template: list[dict],
        date: datetime,
        expired: list[dict]
) -> None:
    with mock.patch("app.main.datetime") as mocked_date:
        mocked_date.date.today.return_value = date
        assert outdated_products(products_template) == expired
