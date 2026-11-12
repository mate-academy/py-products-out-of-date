import datetime


import pytest
from unittest.mock import patch
from typing import List


from app import main


@pytest.mark.parametrize(
    "date, outdated",
    [
        (datetime.date(2022, 1, 1), []),
        (datetime.date(2022, 2, 5), ["duck"]),
        (datetime.date(2022, 2, 10), ["chicken", "duck"]),
        (datetime.date(2022, 2, 11), ["salmon", "chicken", "duck"]),
    ]
)
def test_outdated_products(date: datetime.date, outdated: List[str]) -> None:
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

    with patch("datetime.date") as date_patch:
        date_patch.today.return_value = date
        assert main.outdated_products(products) == outdated
