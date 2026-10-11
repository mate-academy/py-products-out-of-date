from datetime import date
from unittest.mock import patch
import pytest
from app.main import outdated_products


@pytest.mark.parametrize(
    "today_date, expiration_date, expected",
    [
        (date(2022, 2, 2), date(2022, 2, 1), ["duck"]),
        (date(2022, 2, 2), date(2022, 2, 2), []),
        (date(2022, 2, 2), date(2022, 2, 5), []),
    ],
)
@patch("app.main.datetime.date")
def test_outdated_products(
        mock_date: patch,
        today_date: date,
        expiration_date: date,
        expected: list
) -> None:
    mock_date.today.return_value = today_date

    products = [
        {
            "name": "duck",
            "expiration_date": expiration_date,
            "price": 100,
        }
    ]

    assert outdated_products(products) == expected


def test_outdated_products_empty() -> None:
    assert outdated_products([]) == []
