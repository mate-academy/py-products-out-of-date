import pytest

from unittest import mock
from app.main import outdated_products


@pytest.mark.parametrize(
    "products,date,expected",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": "2026-2-10",
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": "2026-2-5",
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": "2026-1-31",
                    "price": 160
                }
            ],
            "2026-2-1",
            ["duck"]
        ),
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": "2026-2-9",
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": "2026-2-5",
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": "2026-1-31",
                    "price": 160
                }
            ],
            "2026-2-6",
            ["chicken", "duck"]
        ),
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": "2026-2-9",
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": "2026-2-5",
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": "2026-1-31",
                    "price": 160
                }
            ],
            "2026-2-9",
            ["chicken", "duck"]
        ),
    ]
)
def test_check_expiration_date(
        products: list,
        date: str,
        expected: list
) -> None:
    with mock.patch("datetime.date") as mock_today:
        mock_today.today.return_value = date
        assert outdated_products(products) == expected
