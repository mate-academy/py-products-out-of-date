import datetime
import pytest
from unittest.mock import patch
from app.main import outdated_products


@pytest.fixture()
def products_template() -> list:
    return [
        {
            "name": "duck",
            "expiration_date": datetime.date(2023, 10, 29),
            "price": 200
        },
        {
            "name": "fish",
            "expiration_date": datetime.date(2023, 10, 29),
            "price": 200
        },
        {
            "name": "rabbit",
            "expiration_date": datetime.date(2023, 10, 29),
            "price": 200
        }
    ]


def test_all_product_fresh(products_template: list) -> None:
    today = datetime.date(2023, 10, 28)
    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = today
        result = outdated_products(products_template)
        assert result == []


def test_expiration_day_today_outdated(products_template: list) -> None:
    today = datetime.date(2023, 10, 29)
    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = today
        result = outdated_products(products_template)
        assert result == [], (
            "Product with expiration date equals today is not outdated."
        )


def test_all_expired(products_template: list) -> None:
    today = datetime.date(2023, 10, 30)
    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = today
        result = outdated_products(products_template)
        assert result == ["duck", "fish", "rabbit"]
