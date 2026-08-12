import datetime
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.fixture()
def product_list() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600},
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120},
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]


@pytest.mark.parametrize(
    "year,month,day,result",
    [
        (2020, 1, 1, []),
        (2022, 2, 2, ["duck"]),
        (2022, 2, 5, ["duck"]),
        (2022, 3, 3, ["salmon", "chicken", "duck"])
    ],
    ids=[
        "Products are not outdated",
        "Some products are outdated",
        "Expiration day is today",
        "All products are outdated"
    ]
)
def test_outdated_products(
        product_list: list, year: int, month: int, day: int, result: list
) -> None:
    from datetime import date

    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = date(year, month, day)

        assert outdated_products(product_list) == result
