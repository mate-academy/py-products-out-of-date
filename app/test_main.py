from datetime import date
from unittest.mock import patch

import pytest
from app import main


@pytest.mark.parametrize(
    "products, expected",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": date(2022, 2, 1),
                    "price": 160
                },
            ],
            ["duck"],
        ),
        (
            [
                {
                    "name": "milk",
                    "expiration_date": date(2022, 2, 2),
                    "price": 100,
                },
            ],
            [],
        ),
    ],
)
@patch("app.main.datetime.date")
def test_outdated_products(
    mock_date: object,
    products: list[dict],
    expected: list[str],
) -> None:
    mock_date.today.return_value = date(2022, 2, 2)

    assert main.outdated_products(products) == expected
