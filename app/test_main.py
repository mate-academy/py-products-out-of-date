from unittest.mock import patch, Mock
import pytest
import datetime
from app.main import outdated_products


@pytest.mark.parametrize(
    "input_products, mock_current_date, expected_products",
    [
        (
                [
                    {
                        "name": "salmon",
                        "expiration_date": datetime.date(2025, 12, 31),
                        "price": 600,
                    }
                ],
                datetime.date(2026, 1, 1),
                ["salmon"],
        ),

        (
                [
                    {
                        "name": "chicken",
                        "expiration_date": datetime.date(2025, 2, 5),
                        "price": 120,
                    }
                ],
                datetime.date(2025, 2, 1),
                [],
        ),

        (
                [
                    {
                        "name": "duck",
                        "expiration_date": datetime.date(2026, 2, 1),
                        "price": 160,
                    }
                ],
                datetime.date(2026, 2, 2),
                ["duck"],
        ),

        (
                [
                    {
                        "name": "cheese",
                        "expiration_date": datetime.date(2025, 10, 20),
                        "price": 50,
                    }
                ],
                datetime.date(2025, 10, 20),
                [],
        ),
    ],
)
@patch("app.main.datetime.date")
def test_outdated_products(input_products: list, mock_current_date: datetime.date, expected_products: list, mock_date: Mock) -> None:
    mock_date.today.return_value = mock_current_date

    result_products = outdated_products(input_products)

    assert result_products == expected_products
