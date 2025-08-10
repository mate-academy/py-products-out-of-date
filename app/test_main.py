from app.main import outdated_products
import datetime
import pytest
from unittest import mock


@pytest.mark.parametrize(
    "products, date",
    [
        (
            [
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
            ], datetime.date(2022, 2, 2),
        )
    ]
)
def test_returning_outdated_products(products: list, date: datetime) -> None:
    with mock.patch("app.main.get_today", return_value=date):
        assert outdated_products(products) == ["duck"]
