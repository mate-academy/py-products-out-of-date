from unittest.mock import MagicMock, patch
import datetime

from app.main import outdated_products


REAL_DATE = datetime.date


@patch("datetime.date")
def test_outdated_products(mock_today: MagicMock) -> None:
    mock_today.today.return_value = REAL_DATE(2022, 2, 5)
    products = [
        {"name": "Expired product", "expiration_date": REAL_DATE(2022, 2, 4)},
        {"name": "Fresh product", "expiration_date": REAL_DATE(2022, 2, 6)},
    ]

    assert outdated_products(products) == ["Expired product"]


@patch("datetime.date")
def test_product_expiring_today_is_not_outdated(mock_today: MagicMock) -> None:
    mock_today.today.return_value = REAL_DATE(2022, 2, 5)
    products = [
        {
            "name": "Product expiring today",
            "expiration_date": REAL_DATE(2022, 2, 5),
        },
    ]

    assert outdated_products(products) == []
