import datetime

import pytest

from app.main import outdated_products

from unittest import mock


real_date = datetime.date


@pytest.mark.parametrize(
    "list_of_products,expired_outdated",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "salo",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 100000
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
            ],
            ["duck"]
        )
    ]
)
@mock.patch("app.main.datetime.date")
def test_outdated_products(
        mocked_datetime_date: mock.MagicMock,
        list_of_products: list,
        expired_outdated: list
) -> None:
    mocked_datetime_date.today.return_value = real_date(2022, 2, 2)
    assert outdated_products(list_of_products) == expired_outdated
