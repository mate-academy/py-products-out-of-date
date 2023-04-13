import datetime
import pytest

from unittest import mock
from app.main import outdated_products


_products = [
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
    "products, expired_date, result",
    [
        (_products, datetime.date(2022, 2, 1), []),
        (_products, datetime.date(2022, 2, 2), ["duck"]),
        (_products, datetime.date(2022, 2, 11), ["salmon", "chicken", "duck"])
    ],
    ids=[
        "test 1: should return empty list",
        "test 2: should return ['duck']",
        "test 3: should return ['salmon', 'chicken', 'duck']"
    ]
)
@mock.patch("datetime.date")
def test_outdated_products(
        mocked_date: mock,
        products: list[dict],
        expired_date: datetime,
        result: list[str],
) -> None:
    mocked_date.today.return_value = expired_date
    assert (
        outdated_products(products) == result
    )
