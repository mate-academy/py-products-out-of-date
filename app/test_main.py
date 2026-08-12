import pytest

from datetime import date
from unittest import mock

from app.main import outdated_products


@pytest.mark.parametrize(
    "products, outdated",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": date(2022, 2, 2),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": date(2022, 2, 1),
                    "price": 160
                }
            ],
            ["duck"]
        )
    ]
)
def test_outdated_products(
        products: list,
        outdated: list
) -> None:
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = date(2022, 2, 2)
        assert outdated_products(products) == outdated
