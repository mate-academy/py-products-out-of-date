from datetime import date
from typing import Any

from app.main import outdated_products
from unittest import mock


@mock.patch("app.main.datetime")
def test_product_list(mock_datetime: Any) -> None:
    mock_datetime.date.today.return_value = date(2022, 2, 2)

    assert outdated_products([
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        }
    ]) == ["duck"]
