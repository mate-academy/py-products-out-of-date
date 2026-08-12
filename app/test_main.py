import pytest
import datetime
from app.main import outdated_products
from unittest import mock


@pytest.mark.parametrize(
    "products, expected",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600,
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120,
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160,
                },
            ],
            ["salmon", "chicken", "duck"],
        ),
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2026, 5, 2),
                    "price": 600,
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120,
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160,
                },
            ],
            ["chicken", "duck"],
        ),
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2026, 5, 1),
                    "price": 600,
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2026, 5, 1),
                    "price": 120,
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2026, 5, 1),
                    "price": 160,
                },
            ],
            ["salmon", "chicken", "duck"],
        ),
    ],
)
def test_outdated_products(products: list, expected: list) -> None:
    fake_today = datetime.date(2026, 5, 2)

    with mock.patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = fake_today

        assert outdated_products(products) == expected
