import pytest
from unittest import mock
import datetime

from app.main import outdated_products


@pytest.mark.parametrize(
    "today, products, expected",
    [
        (
            datetime.date(2022, 2, 1),
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
                }
            ],
            []
        ),
        (
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 3),
                    "price": 160
                }
            ],
            ["chicken"]
        ),
        (
            datetime.date(2022, 2, 5),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 3),
                    "price": 600},
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 120},
            ],
            ["salmon", "chicken"]
        ),
        (
            datetime.date(2022, 2, 5),
            [],
            []
        ),
        (
            datetime.date(2022, 2, 1),
            [
                {
                    "name": "apple",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 10
                },
                {
                    "name": "banana",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 20}
            ],
            []
        ),
    ]
)
def test_should_return_outdated_products(
        today: datetime,
        products: list,
        expected: list
) -> None:
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = today

        assert outdated_products(products) == expected
