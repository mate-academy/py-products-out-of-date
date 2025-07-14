import datetime
from unittest.mock import patch

import pytest

from app.main import outdated_products


class DateMock(datetime.date):
    _today = None

    @classmethod
    def today(cls) -> datetime.date:
        return cls._today


@pytest.mark.parametrize(
    "fixed_today, incoming_list_of_products, expected_result",
    [
        (
            datetime.date(2025, 7, 14),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2025, 7, 24),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2025, 7, 16),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2025, 7, 11),
                    "price": 160
                }
            ],
            ["duck"],
        ),
        (
            datetime.date(2025, 7, 14),
            [
                {
                    "name": "apples",
                    "expiration_date": datetime.date(2025, 7, 13),
                    "price": 130
                },
                {
                    "name": "oranges",
                    "expiration_date": datetime.date(2025, 7, 10),
                    "price": 170
                }
            ],
            ["apples", "oranges"],
        ),
        (
            datetime.date(2025, 7, 14),
            [
                {
                    "name": "herring",
                    "expiration_date": datetime.date(2025, 7, 14),
                    "price": 245
                },
                {
                    "name": "canned sardines",
                    "expiration_date": datetime.date(2029, 11, 3),
                    "price": 190
                }
            ],
            [],
        ),
    ]
)
def test_should_return_correct_list_with_outdated_products(
    fixed_today: datetime.date,
    incoming_list_of_products: list,
    expected_result: list,
) -> None:
    DateMock._today = fixed_today
    with patch("app.main.datetime.date", DateMock):
        result = outdated_products(incoming_list_of_products)
    assert result == expected_result
