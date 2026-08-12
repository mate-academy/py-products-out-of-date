import datetime
import pytest
from app.main import outdated_products
from unittest import mock


@pytest.mark.parametrize(
    "products, outdated",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600,
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120,
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160,
                },
            ],
            ["duck"],
        )
    ],
)
def test_outdated_products(products: list, outdated: list) -> None:
    with mock.patch("app.main.datetime") as mock_date:
        mock_date.date.today.return_value = datetime.date(2022, 2, 2)
        assert outdated_products(products) == outdated
