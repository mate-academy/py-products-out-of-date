from unittest.mock import patch
import pytest
from datetime import date
from typing import List
from app.main import outdated_products


@pytest.fixture()
def products() -> List[dict]:
    return [
        {
            "name": "hamon",
            "expiration_date": date(2026, 2, 1),
            "price": 700
        },
        {
            "name": "bread",
            "expiration_date": date(2025, 8, 28),
            "price": 25
        },
        {
            "name": "banana",
            "expiration_date": date(2025, 8, 27),
            "price": 20
        },
        {
            "name": "cherry",
            "expiration_date": date(2025, 8, 26),
            "price": 10
        },
        {
            "name": "chips",
            "expiration_date": date(2020, 1, 1),
            "price": 45
        }
    ]


def test_outdated_products(products: List[dict]) -> None:
    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = date(2025, 8, 27)
        assert outdated_products(products) == ["cherry", "chips"]
