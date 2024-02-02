import pytest
import datetime

from unittest.mock import patch
from app.main import outdated_products

products = [
    {
        "name": "salmon",
        "expiration_date": datetime.date(2022, 2, 10),
        "price": 600
    },
    {
        "name": "chicken",
        "expiration_date": datetime.date(2022, 2, 5),
        "price": 120
    },
    {
        "name": "duck",
        "expiration_date": datetime.date(2022, 2, 1),
        "price": 160
    }
]


@pytest.mark.parametrize(
    "expected_date,expected_names",
    [
        (
            datetime.date(2022, 2, 6),
            ["chicken", "duck"],
        ),
        (
            datetime.date(2022, 2, 5),
            ["duck"],
        ),
        (
            datetime.date(2022, 2, 11),
            ["salmon", "chicken", "duck"],
        ),
        (
            datetime.date(2022, 1, 31),
            [],
        ),

    ],
    ids=[
        "Today is 2022-02-06, two product outdated (chicken, duck)",
        "Today is 2022-02-05, one products outdated (duck)",
        "Today is 2022-02-11, three products outdated (salmon, chicken, duck)",
        "Today is 2022-01-31, no products outdated!",
    ]
)
def test_outdated_products(
    expected_date: datetime.date,
    expected_names: list[str],
) -> None:

    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = expected_date

        assert outdated_products(products) == expected_names
