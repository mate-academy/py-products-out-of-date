import datetime
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "today_date,product_list,expected",
    [
        (
            datetime.date(2024, 2, 11),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2024, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2024, 2, 5),
                    "price": 120
                }
            ],
            ["salmon", "chicken"]
        ),
        (
            datetime.date(2024, 2, 10),
            [
                {
                    "name": "carrot",
                    "expiration_date": datetime.date(2024, 2, 10),
                    "price": 50
                },
                {
                    "name": "apple",
                    "expiration_date": datetime.date(2024, 2, 5),
                    "price": 60
                },
                {
                    "name": "pear",
                    "expiration_date": datetime.date(2024, 2, 1),
                    "price": 80
                }
            ],
            ["apple", "pear"]
        ),
        (
            datetime.date(2024, 1, 2),
            [
                {
                    "name": "milk",
                    "expiration_date": datetime.date(2024, 2, 10),
                    "price": 67
                },
                {
                    "name": "yogurt",
                    "expiration_date": datetime.date(2024, 2, 5),
                    "price": 95
                }
            ],
            []
        ),
        (
            datetime.date(2023, 3, 2),
            [],
            []
        )
    ],
    ids=[
        "should return all expired products",
        "should not return products with today date",
        "should return empty list if no expired products",
        "should return empty list if product list is empty"
    ]
)
@mock.patch("app.main.datetime.date")
def test_outdated_products(
        mock_datetime_date: mock.MagicMock,
        today_date: datetime.date,
        product_list: list[dict],
        expected: list[str]
) -> None:
    mock_datetime_date.today.return_value = today_date
    assert outdated_products(product_list) == expected
