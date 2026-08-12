import datetime

import pytest
from unittest import mock

from app.main import outdated_products


@pytest.mark.parametrize(
    "products,today,expected",
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
                },
                {
                    "name": "fish",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 240
                }

            ],
            datetime.date(2022, 2, 2),
            ["duck"]
        )
    ]
)
def test_outdated_products(products: list[dict],
                           today: datetime.date,
                           expected: list[str]
                           ) -> None:
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = today
        assert outdated_products(products) == expected
