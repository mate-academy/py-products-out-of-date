from app.main import outdated_products
import datetime
from unittest.mock import patch, Mock
import pytest


@pytest.mark.parametrize(
    "product_list, today_date, expected",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600},
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 120},
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                },
            ],
            datetime.date(2022, 2, 2),
            ["duck"],
        ),
    ]
)
@patch("app.main.datetime.date")
def test_outdated_products(
        mock_date: Mock, product_list: list,
        today_date: datetime.date, expected: list) -> None:
    mock_date.today.return_value = today_date
    assert outdated_products(product_list) == expected
