import pytest
import datetime
from unittest import mock
from unittest.mock import MagicMock
import app.main as main


@pytest.fixture()
def product_details() -> list[dict]:
    return [
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


@mock.patch("app.main.datetime")
def test_one_outdated_products(
        mock_date_today: MagicMock,
        product_details: list
) -> None:
    mock_date_today.date.today.return_value = datetime.date(2022, 2, 1)
    product = product_details
    assert main.outdated_products(product) == []
