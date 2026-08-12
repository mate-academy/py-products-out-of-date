import pytest
import datetime
from unittest.mock import patch, MagicMock
from app.main import outdated_products


@pytest.mark.parametrize(
    "products, expected_result",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2026, 7, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2026, 3, 1),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2026, 6, 11),
                    "price": 160
                },
                {
                    "name": "milk",
                    "expiration_date": datetime.date(2026, 6, 9),
                    "price": 40
                },
                {
                    "name": "cheese",
                    "expiration_date": datetime.date(2026, 6, 10),
                    "price": 80
                }
            ],

            ["chicken", "milk"],
        ),
    ],
    ids=[
        "should delete outstanding product"
    ]
)
@patch("app.main.datetime.datetime")
def test_outdated_products(
        mock_datetime: MagicMock,
        products: list,
        expected_result: list
) -> None:
    mock_datetime.today.return_value = datetime.date(2026, 6, 10)
    assert outdated_products(products) == expected_result
