import pytest
from app.main import outdated_products
from unittest import mock
from datetime import date


@pytest.fixture()
def products() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": date(2023, 5, 20),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2023, 5, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2023, 5, 1),
            "price": 160
        }
    ]


@mock.patch("app.main.datetime.date.today")
def test_outdated_products_equals_today(
        mock_date: mock.Mock,
        products: list[dict]
) -> None:
    mock_date.return_value = date(2023, 5, 10)
    assert outdated_products(products) == ["chicken", "duck"]
