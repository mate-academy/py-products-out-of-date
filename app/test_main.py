import datetime
from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "products, current_date, expected_result",
    [
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2024, 2, 20),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2024, 2, 18),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2024, 2, 17),
                    "price": 160
                }
            ],
            datetime.date(2024, 2, 18),
            ["duck"],
            id="should return list with outdated products names"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2024, 2, 20),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2024, 2, 18),
                    "price": 120
                },
            ],
            datetime.date(2024, 2, 18),
            [],
            id="should return empty list if no outdated products"
        )
    ]
)
@mock.patch("app.main.datetime.date")
def test_outdated_products(
        mocked_date_today: MagicMock,
        products: list,
        current_date: datetime,
        expected_result: list
) -> None:
    mocked_date_today.today.return_value = current_date

    result = outdated_products(products)

    assert result == expected_result
