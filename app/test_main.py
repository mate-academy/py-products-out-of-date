from datetime import date, timedelta
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "product,expected",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": date(2026, 3, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": date(2028, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": date(2026, 3, 13),
                    "price": 160
                },
            ],
            [
                "salmon",
            ],
        ),
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": date(2026, 3, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": date.today() - timedelta(days=1),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": date(2026, 3, 13),
                    "price": 160
                },
            ],
            [
                "salmon",
            ],
        ),
    ],
)
def test_outdated_products(product: list, expected: list) -> None:
    with mock.patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = date(2026, 3, 11)
        mock_date.side_effect = lambda *args, **kwargs: date(*args, **kwargs)
        assert outdated_products(product) == expected
