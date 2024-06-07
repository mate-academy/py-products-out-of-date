from app.main import outdated_products
from unittest import mock
import datetime
import pytest


@pytest.fixture()
def product() -> None:
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


def test_outdated_products(product: list) -> None:
    with mock.patch("datetime.date") as mock_datetime:
        mock_datetime.return_value = datetime.date(2022, 2, 1)
        assert outdated_products(product) == ["duck"]
