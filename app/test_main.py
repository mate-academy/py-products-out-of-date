import datetime
import pytest
from unittest import mock

from app.main import outdated_products


@pytest.mark.parametrize(
    "products, expected_list",
    [
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10)
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5)
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 3)
                }
            ],
            [],
            id="no products out date"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10)
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5)
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1)
                }
            ],
            ["duck"],
            id="one product out date"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 1)
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 1)
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1)
                }
            ],
            ["salmon", "chicken", "duck"],
            id="all products out date"
        )
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(mocked_datetime, products, expected_list):
    mocked_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products) == expected_list
