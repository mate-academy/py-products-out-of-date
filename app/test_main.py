import datetime
from unittest.mock import MagicMock

import pytest
from unittest import mock

from app.main import outdated_products


@pytest.mark.parametrize(
    "products,today_date,result",
    [
        ([
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
        ], datetime.date(2022, 2, 2), ["duck"]),
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 600
                }
            ], datetime.date(2022, 2, 2), [],
        ),
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 3),
                    "price": 600
                }
            ], datetime.date(2022, 2, 2), [],
        ),
        ([], datetime.date(2022, 2, 2), [])
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(mock_date: MagicMock,
                           products: list[dict],
                           today_date: datetime.date,
                           result: list[dict]) -> None:
    mock_date.date.today.return_value = today_date
    assert outdated_products(products) == result
