from unittest import mock
import datetime

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "products,result",
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
                    "expiration_date": datetime.date(2022, 2, 4),
                    "price": 120
                },
                {
                    "name": "bread",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ],
            ["chicken", "duck"]
        ),
    ]
)
def test_outdated_products(products: list[dict],
                           result: list[str]) -> None:
    with mock.patch("app.main.datetime.date",
                    wraps=datetime.date) as mock_date:
        mock_date.today.return_value = datetime.date(2022, 2, 5)
        assert outdated_products(products) == result
