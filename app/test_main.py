import pytest
from datetime import date
from unittest.mock import patch

from app.main import outdated_products


@pytest.mark.parametrize(
    "current_date, products, expected_result",
    [
        (
            date(2022, 2, 2),
            [
                {
                    "name": "salmon",
                    "expiration_date": date(2022, 2, 10),
                    "price": 600},
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
        ),
        (
            date(2022, 2, 2),
            [
                {
                    "name": "salmon",
                    "expiration_date": date(2022, 2, 10),
                    "price": 600},
                {
                    "name": "chicken",
                    "expiration_date": date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": date(2022, 2, 2),
                    "price": 160
                }
            ],
            []
        )
    ]
)
def test_can_access_google_page_accessible(
        current_date: date,
        products: list[dict],
        expected_result: list
) -> None:
    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = current_date
        result = outdated_products(products)

    assert result == expected_result
