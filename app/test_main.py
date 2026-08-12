import datetime
import pytest

from app.main import outdated_products

from unittest import mock


@pytest.mark.parametrize(
    "value, output",
    [
        (
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
            [
                "duck"
            ]
        ),
        (
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
                    "expiration_date": datetime.date(2022, 2, 3),
                    "price": 160
                }
            ],
            []
        )
    ]
)
@mock.patch("app.main.datetime")
def test_return_outdated_product(
    mock_date: datetime,
    value: list,
    output: list
) -> list:
    mock_date.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(value) == output
