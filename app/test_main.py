from unittest import mock
import datetime

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "products, result",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2024, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2024, 9, 4),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2024, 9, 3),
                    "price": 160
                }
            ],
            ["salmon", "duck"]
        )
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(
        mock_datetime: mock.MagicMock,
        products: list[dict],
        result: list
) -> None:
    mock_datetime.date.today.return_value = datetime.date(2024, 9, 4)
    assert outdated_products(products) == result
