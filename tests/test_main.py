import datetime
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "products, expected",
    [
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 10, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 5, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ],
            ["duck"],
            id="Test for out of date duck"
        ),
        pytest.param(
            [],
            [],
            id="Test empty list"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2012, 10, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2010, 5, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ],
            ['salmon', 'chicken', 'duck'],
            id="Test for all out of date"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2012, 10, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2010, 5, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                },
                {
                    "name": "milk",
                    "expiration_date": datetime.date(2022, 2, 3),
                    "price": 120
                },
                {
                    "name": "cheese",
                    "expiration_date": datetime.date(2030, 1, 1),
                    "price": 120
                },
                {
                    "name": "cottage cheese",
                    "expiration_date": datetime.date(2022, 1, 12),
                    "price": 120
                },
                {
                    "name": "avocado",
                    "expiration_date": datetime.date(2021, 7, 29),
                    "price": 120
                },
                {
                    "name": "bread",
                    "expiration_date": datetime.date(2022, 1, 29),
                    "price": 120
                },

            ],
            [
                'salmon',
                'chicken',
                'duck',
                "milk",
                "cottage cheese",
                "avocado",
                "bread"
            ],
            id="Test big list"
        ),
        pytest.param(
            [
                {
                    "name": "nuclear salmon",
                    "expiration_date": datetime.date(2023, 10, 10),
                    "price": 600
                },
                {
                    "name": "nuclear chicken",
                    "expiration_date": datetime.date(2023, 5, 5),
                    "price": 120
                },
                {
                    "name": "nuclear duck",
                    "expiration_date": datetime.date(2023, 2, 1),
                    "price": 160
                }
            ],
            [],
            id="Test for not out of date"
        )

    ],
)
@mock.patch("app.main.datetime")
def test_outdated_products(mocked_time, products, expected):
    mocked_time.date.today = mock.Mock(
        return_value=datetime.date(2022, 2, 4)
    )
    mocked_time.date.today()

    assert outdated_products(products) == expected
