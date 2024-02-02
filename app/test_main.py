import pytest
import datetime

from unittest.mock import patch
from app.main import outdated_products


@pytest.mark.parametrize(
    "expected_date,expected_names",
    [
        (
            datetime.date(2024, 1, 28),
            ["duck"],
        ),
        (
            datetime.date(2024, 2, 6),
            ["chicken", "duck"],
        ),
        (
            datetime.date(2024, 2, 11),
            ["salmon", "chicken", "duck"],
        ),
        (
            datetime.date(2024, 1, 1),
            [],
        ),
    ],
    ids=[
        "Today is 2024-01-28, one product outdated (duck)",
        "Today is 2024-02-06, two products outdated (chicken, duck)",
        "Today is 2024-02-11, three products outdated (salmon, chicken, duck)",
        "Today is 2024-01-01, no products outdated",
    ]
)
def test_outdated_products(
    expected_date: datetime.date,
    expected_names: list[str],
) -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2024, 2, 10),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2024, 2, 5),
            "price": 120},
        {
            "name": "duck",
            "expiration_date": datetime.date(2024, 1, 22),
            "price": 160,
        },
    ]

    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = expected_date

        assert outdated_products(products) == expected_names
        mock_date.assert_called_once()
