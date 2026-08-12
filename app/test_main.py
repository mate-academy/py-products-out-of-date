import datetime
from unittest import mock
from app.main import outdated_products
import pytest


@pytest.mark.parametrize(
    "products,result,date",
    [
        ([
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
         }],
         ["duck"],
         (2022, 2, 2))
    ]
)
def test_main(products: list, result: list, date: tuple) -> None:
    with mock.patch("app.main.datetime") as mocked_date:
        mocked_date.date.today.return_value = datetime.date(*date)
        assert outdated_products(products) == result
