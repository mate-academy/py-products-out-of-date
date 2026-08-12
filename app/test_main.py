import datetime
from unittest import mock

import pytest

from app.main import outdated_products


@mock.patch("app.main.datetime")
@pytest.mark.parametrize(
    "products, result",
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
        ], ["duck"])

    ]
)
def test_outdated_products(mock_date: datetime,
                           products: list[dict],
                           result: list[str]) -> None:

    mock_date.date.today.return_value = datetime.date(2022, 2, 2)

    assert outdated_products(products) == result
