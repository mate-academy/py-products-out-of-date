import pytest
from app.main import outdated_products
from unittest import mock
import datetime


@pytest.mark.parametrize(
    "products, expected",
    [
        pytest.param(
            [
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
            ["duck"],
            id="only duck outdated"
        ),
        pytest.param(
            [
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
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 160
                }
            ],
            [],
            id="without outdated products"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2020, 2, 2),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 1, 2),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ],
            ["salmon", "chicken", "duck"],
            id="all products are outdated"
        ),
    ]
)
@ mock.patch("app.main.datetime")
def test_outdated_products(mocked_time,
                           products,
                           expected):
    mocked_time.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products) == expected
