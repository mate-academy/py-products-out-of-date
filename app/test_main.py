from datetime import date
from unittest.mock import patch, MagicMock

from app.main import outdated_products


@patch("app.main.datetime.date")
def test_outdated_products(mocked_today: MagicMock) -> None:
    product = [
        {"name": "chips", "expiration_date": date(2022, 2, 16)}
    ]
    mocked_today.today.return_value = date(2022, 2, 17)
    assert outdated_products(product) == ["chips"]


@patch("app.main.datetime.date")
def test_not_outdated_products(mocked_today: MagicMock) -> None:
    product = [
        {"name": "Nesquik", "expiration_date": date(2022, 2, 3)}
    ]
    mocked_today.today.return_value = date(2022, 2, 2)
    assert outdated_products(product) == []


@patch("app.main.datetime.date")
def test_the_product_expires_today(mocked_today: MagicMock) -> None:
    product = [
        {"name": "cocacola", "expiration_date": date(2022, 2, 2)}
    ]
    mocked_today.today.return_value = date(2022, 2, 2)
    assert outdated_products(product) == []
