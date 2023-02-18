import datetime

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "products,result",
    [
        ([{"name": "duck",
           "expiration_date": datetime.date(2023, 2, 19),
           "price": 120}], []),
        ([{"name": "chicken",
           "expiration_date": datetime.date(2023, 2, 18),
           "price": 120}], []),
        ([{"name": "duck",
           "expiration_date": datetime.date(2023, 2, 17),
           "price": 160}], ["duck"])
    ]
)
def test_outdated_products(products: list, result: list) -> None:
    assert outdated_products(products) == result
