import pytest
import datetime
from app.main import outdated_products
from unittest.mock import patch


@pytest.mark.parametrize("products, result", [
    ([
        {
            "name":
            "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        }
    ], []),
    ([
        {
            "name":
            "chicken",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 120
        }
    ], ["chicken"]),
    ([
        {
            "name":
            "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name":
            "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name":
            "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ], ["duck"])
])
def test_outdated_products(products: list, result: list) -> None:
    with patch("app.main.datetime") as mock_dt:
        mock_today = datetime.date(2022, 2, 2)
        mock_dt.date.today.return_value = mock_today
        assert outdated_products(products) == result
