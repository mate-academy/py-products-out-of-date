from unittest import mock

from datetime import date

import pytest

from app.main import outdated_products


@pytest.fixture
def mock_today_date() -> date:
    return date(2022, 2, 2)


@pytest.mark.parametrize(
    "products, expected_outdated",
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
                    }
                ],
                ["duck"]
        ),

    ]
)
def test_outdated_products(
        mock_today_date: date,
        products: list,
        expected_outdated: list) -> None:
    with mock.patch("app.main.date") as mock_date:
        mock_date.today.return_value = mock_today_date
        result = outdated_products(products)
        assert result == expected_outdated
