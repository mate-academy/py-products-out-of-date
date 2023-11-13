import pytest
import datetime
from unittest import mock
from app.main import outdated_products


@pytest.mark.parametrize(
    "products, expected",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2024, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2023, 11, 13),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2023, 11, 12),
                    "price": 160
                }
            ],
            ["duck"]
        )
    ]
)
def test_outdated_products(
        products: list,
        expected: list,
) -> None:
    with mock.patch("datetime.datetime") as mock_date:
        mock_date.date.today.return_value = datetime.date.today()
        print(mock_date.date.today.return_value)
        assert outdated_products(products) == expected
