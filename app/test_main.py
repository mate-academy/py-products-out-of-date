# write your code here
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
    "products, date, expired",
    [
        (products, datetime.date(2022, 1, 13), []),
        (products, datetime.date(2022, 3, 13), [
            "salmon", "chicken", "duck"
        ]),
        (products, datetime.date(2022, 2, 3), ["duck"])

    ],
    ids=[
        "All good",
        "All is spoiled",
        "Duck didn`t make it"
    ]
)
def test_outdated_products(
        products: list, date: datetime, expired: list
) -> None:
    with mock.patch("app.main.datetime") as mocked_date:
        mocked_date.date.today.return_value = date
        assert outdated_products(products) == expired
