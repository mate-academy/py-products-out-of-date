import datetime
from unittest.mock import patch

import pytest

from app.main import outdated_products

list_of_products = [
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
    "today_date, result",
    [
        (datetime.date(1800, 1, 1), []),
        (datetime.date(2800, 1, 1), ["salmon", "chicken", "duck"]),
        (datetime.date(2022, 2, 10), ["chicken", "duck"]),
    ]
)
def test_outdated_products(today_date: datetime.date, result: list) -> None:
    with patch("app.main.datetime") as mock_date_today:
        mock_date_today.date.today.return_value = today_date
        assert outdated_products(list_of_products) == result
