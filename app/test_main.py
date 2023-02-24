import datetime
from unittest import mock

import pytest
from app.main import outdated_products

pr = [
    {
        "name": "apple",
        "expiration_date": datetime.date(2023, 2, 23),
        "price": 10
    },
    {
        "name": "banana",
        "expiration_date": datetime.date(2023, 2, 24),
        "price": 20
    },
    {
        "name": "orange",
        "expiration_date": datetime.date(2023, 2, 25),
        "price": 30
    },
]


@pytest.fixture()
def mocked_date() -> mock.Mock:
    with mock.patch("datetime.date") as mock_date:
        yield mock_date.today


@pytest.mark.parametrize(
    "products,date,expected_result",
    [
        (pr, datetime.date(2023, 2, 23), []),
        (pr, datetime.date(2023, 2, 24), ["apple"]),
        (pr, datetime.date(2023, 2, 25), ["apple", "banana"]),
        (pr, datetime.date(2023, 2, 26), ["apple", "banana", "orange"]),
    ]
)
def test_outdated_products(
        mocked_date: mock.Mock,
        products: list[dict],
        date: datetime.date,
        expected_result: list[str]
) -> None:
    mocked_date.return_value = date
    assert outdated_products(products) == expected_result
