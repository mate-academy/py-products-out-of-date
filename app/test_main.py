from unittest import mock

import pytest
import datetime

from app.main import outdated_products


@mock.patch("app.main.datetime")
@pytest.mark.parametrize(
    "products,date,expected_result",
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
            ],
            datetime.date(2022, 2, 2),
            ["duck"]
        )
    ]
)
def test_outdated_products(mock_date: datetime,
                           products: list[dict],
                           date: datetime.date,
                           expected_result: list[str]) -> None:
    mock_date.date.today.return_value = date
    assert outdated_products(products) == expected_result
