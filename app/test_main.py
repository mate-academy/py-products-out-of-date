import pytest
import datetime
from unittest import mock
from app import main


product_case1 = [
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
    }
]
product_case2 = [
    {
        "name": "milk",
        "expiration_date": datetime.date(2022, 1, 1),
        "price": 20,
    },
    {
        "name": "bread",
        "expiration_date": datetime.date(2022, 2, 3),
        "price": 10,
    }
]


@pytest.mark.parametrize(
    "today_value,products,expected",
    [
        (datetime.date(2022, 2, 2), product_case1, ["duck"]),
        (datetime.date(2022, 2, 6), product_case1, ["chicken", "duck"]),
        (datetime.date(2022, 2, 1), product_case2, ["milk"]),
    ]
)
def test_main(today_value: int, products: list, expected: list) -> None:
    with mock.patch("app.main.datetime") as mock_date:
        mock_date.date.today.return_value = today_value
        assert main.outdated_products(products) == expected
