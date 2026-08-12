import pytest
import datetime
from unittest import mock

from app.main import outdated_products


@pytest.mark.parametrize(
    "today, products, expected",
    [
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
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                },
            ],
            ["duck", ],
        ),
        (
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "cheese",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 600
                },
            ],
            [],
        ),
    ]
)
def test_outdated_products(today: datetime.date, products: list,
                           expected: list) -> None:
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = today
        assert outdated_products(products) == expected
