from unittest import mock

import pytest

from app.main import outdated_products
from app.main import datetime


@pytest.mark.parametrize(
    ("data,expected"),
    [
        pytest.param(
            [
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
            ,
            ["duck"]
        )
    ]
)
@mock.patch("app.main.datetime")
def test_params(
        mocked_today: type(object),
        data: list,
        expected: list
) -> None:
    mocked_today.date.today.return_value = datetime.date(2022, 2, 3)
    assert outdated_products(data) == expected
