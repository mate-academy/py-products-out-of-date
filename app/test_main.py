import datetime
import pytest

from unittest.mock import patch
from app.main import outdated_products

products = [
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


@pytest.mark.parametrize(
    "all_products, today_time, dated_products",
    [(products, datetime.date(2022, 2, 3), ["duck"])]
)
def test_outdated_products(all_products: list,
                           today_time: type(datetime),
                           dated_products: list) -> None:
    with patch("app.main.datetime") as mock_datetime:
        mock_datetime.date.today.return_value = today_time
        assert outdated_products(all_products) == dated_products
