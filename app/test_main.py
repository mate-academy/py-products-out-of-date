import pytest
from datetime import date
from unittest.mock import patch
from app.main import outdated_products


PRODUCTS_DATA = [
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
    {"name": "duck",
     "expiration_date": date(2022, 2, 1),
     "price": 160
     },
]


@pytest.mark.parametrize(
    "mock_today_date, expected_outdated_names",
    [
        (date(2022, 2, 2), ["duck"]),
        (date(2022, 2, 5), ["duck"]),
        (date(2022, 2, 6), ["chicken", "duck"]),
        (date(2022, 2, 11), ["salmon", "chicken", "duck"]),
        (date(2022, 1, 31), []),
    ]
)
def test_outdated_products(
        mock_today_date: date,
        expected_outdated_names: list
) -> None:
    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = mock_today_date
        assert outdated_products(PRODUCTS_DATA) == expected_outdated_names
