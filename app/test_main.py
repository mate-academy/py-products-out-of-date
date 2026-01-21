import datetime
from unittest import mock

from app.main import outdated_products
import pytest


@pytest.mark.parametrize(
    "products,expected",
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
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                },
                {
                    "name": "bread",
                    "expiration_date": datetime.date(2022, 1, 3),
                    "price": 110
                },
                {
                    "name": "sausage",
                    "expiration_date": datetime.date(2022, 3, 2),
                    "price": 90
                },
            ],
            [
                "duck",
                "bread",
            ]
        )
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(
        mocked_date: mock.MagicMock,
        products: list[dict],
        expected: list[str]
) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products) == expected
