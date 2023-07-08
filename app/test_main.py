import datetime
import pytest

from unittest.mock import patch

from app.main import outdated_products


@pytest.mark.parametrize(
    "day,products_out_of_date",
    [
        (13, []),
        (14, ["duck"]),
        (15, ["chicken", "duck"]),
        (21, ["salmon", "chicken", "duck"]),
    ],
    ids=[
        "No outdated products",
        "One outdated product",
        "Multiple outdated products",
        "All products outdated",
    ]
)
def test_outdated_products(
    day: int,
    products_out_of_date: list[str]
) -> None:

    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 6, 20),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2023, 6, 14),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2023, 6, 13),
            "price": 160
        }
    ]

    mock_today = datetime.date(2023, 6, day)
    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = mock_today

        assert outdated_products(products) == products_out_of_date
