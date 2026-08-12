import datetime
import unittest.mock

from pytest import mark, param
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


@mark.parametrize(
    "date, product, out",
    [
        param(
            datetime.date(2021, 2, 5),
            products,
            [],
            id="All product is good"
        ),
        param(
            datetime.date.today(),
            products,
            ["salmon", "chicken", "duck"],
            id="All products are expired"
        )
    ]
)
def test_outdated_products_today(
        date: datetime,
        product: list,
        out: list
) -> None:
    with unittest.mock.patch("app.main.datetime") as mock_date:
        mock_date.date.today.return_value = date
        assert outdated_products(products) == out
