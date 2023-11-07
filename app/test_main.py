import pytest

from unittest.mock import patch

from app.main import outdated_products

from datetime import date


@pytest.mark.parametrize(
    "products, expected_outdated", [
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
                }
            ],
            ["duck"]
        )
    ]
)
def test_outdated_products(
        products: list,
        expected_outdated: list
) -> None:
    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = date(2022, 2, 2)

        assert outdated_products(products) == expected_outdated
