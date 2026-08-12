import datetime
from app.main import outdated_products
from unittest.mock import patch, MagicMock
import pytest


@pytest.mark.parametrize("mock_today, products, result", [
    (
        datetime.date(2025, 1, 28),
        [
            {"name": "salmon",
             "expiration_date": datetime.date(2025, 1, 27),
             "price": 600},
            {"name": "duck",
             "expiration_date": datetime.date(2025, 1, 30),
             "price": 160}
        ],
        ["salmon"]
    ),
    (
        datetime.date(2025, 1, 28),
        [
            {"name": "salmon",
             "expiration_date": datetime.date(2025, 1, 28),
             "price": 600},
            {"name": "duck",
             "expiration_date": datetime.date(2025, 1, 30),
             "price": 160}
        ],
        []
    ),
])
@patch("app.main.datetime.date")
def test_outdated_products(mock_date: MagicMock,
                           products: list[dict],
                           result: list[str],
                           mock_today: datetime.date) -> None:
    mock_date.today.return_value = mock_today
    assert (outdated_products(products)
            == result), f"Result is not as expected: {result}"
