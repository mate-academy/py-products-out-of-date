import pytest
import datetime
from unittest import mock
from app.main import outdated_products
from typing import List


@pytest.mark.parametrize(
    "products, mock_today, expected",
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
            datetime.date(2022, 2, 2),
            ["duck"]
        )
    ]
)
def test_outdated_products(
        products: List[dict], mock_today: datetime.date, expected: List[str]
) -> None:
    with mock.patch("app.main.datetime") as mock_date:
        mock_date.date.today.return_value = mock_today
        assert outdated_products(products) == expected
