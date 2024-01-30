from app.main import outdated_products
import datetime
from unittest import mock
import pytest


@pytest.mark.parametrize (
    "products,result",
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
            }
        ],
        ["duck"]),
    ],
    ids=[
        "For 'duck' expiration date out the date "
    ]
)
def test_outdated_products(products: list, result: list) -> None:
    with mock.patch("datetime.date.today()") as mock_date:
        mock_date.return_value = datetime.date(2022, 2, 2)
        assert outdated_products(products= products) == result
