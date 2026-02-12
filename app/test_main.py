import pytest
import datetime
from unittest import mock

from app.main import outdated_products


@mock.patch("app.main.datetime")
@pytest.mark.parametrize(
    "products,expected_result",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2026, 2, 13),
                    "price": 600,
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2026, 2, 12),
                    "price": 120,
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2026, 2, 11),
                    "price": 160,
                },
            ],
            ["duck"],
        )
    ],
)
def test_main(
    mocked_datetime: mock.MagicMock, products: dict, expected_result: list
) -> None:
    mocked_datetime.date.today.return_value = datetime.date(2026, 2, 12)
    assert outdated_products(products) == expected_result
