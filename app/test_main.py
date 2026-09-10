import datetime
import pytest
from unittest import mock

from app.main import outdated_products


products = [
    {
        "name": "salmon",
        "expiration_date": datetime.date(2028, 9, 10),
        "price": 600
    },
    {
        "name": "chicken",
        "expiration_date": datetime.date(2028, 9, 5),
        "price": 120
    },
    {
        "name": "duck",
        "expiration_date": datetime.date(2028, 9, 1),
        "price": 160
    }
]


@pytest.mark.parametrize(
    "test_products, today, expected",
    [
        (
            products,
            datetime.date(2028, 9, 11),
            ["salmon", "chicken", "duck"]
        ),
        (
            products,
            datetime.date(2028, 9, 10),
            ["chicken", "duck"]
        )
    ],
    ids=[
        "all products outdated",
        "expiration_date = today"
    ]
)
@mock.patch("app.main.datetime.date")
def test_outdated_products(
        mock_date: mock.Mock,
        test_products: list[dict],
        today: datetime.date,
        expected: list[str]
) -> None:
    mock_date.today.return_value = today
    assert outdated_products(test_products) == expected
