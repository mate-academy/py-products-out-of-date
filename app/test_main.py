import datetime
from unittest import mock

import pytest

from .main import outdated_products


@pytest.fixture()
def products_template() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600},
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120},
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]


@pytest.mark.parametrize(
    "date_today, result",
    [
        (datetime.date(2022, 2, 10), ["chicken", "duck"]),
        (datetime.date(2022, 2, 11), ["salmon", "chicken", "duck"]),
        (datetime.date(2022, 1, 30), []),
    ]
)
@mock.patch("datetime.date")
def test_outdated_products(
        mocked_date: mock,
        date_today: datetime.date,
        result: list,
        products_template: list,
) -> None:
    mocked_date.today.return_value = date_today
    assert outdated_products(products_template) == result
