import pytest

import datetime

from unittest import mock

from app.main import outdated_products


products = [
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
    "available_products, date, result",
    [
        (products, datetime.date(2022, 2, 1), []),
        (products, datetime.date(2022, 2, 2), ["duck"]),
        (products, datetime.date(2022, 2, 6), ["chicken", "duck"]),
        (products, datetime.date(2022, 2, 11), ["salmon", "chicken", "duck"])
    ]
)
@mock.patch("datetime.date")
def test_outdated_products(
        mocked_date: mock,
        available_products: list,
        date: datetime,
        result: list
) -> None:
    mocked_date.today.return_value = date
    assert outdated_products(products) == result
