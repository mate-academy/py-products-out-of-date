import pytest

import datetime

from unittest import mock

from app.main import outdated_products


@pytest.mark.parametrize(
    "products,date_of_today,outed_product",
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
            datetime.date(2022, 2, 1),
            []
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
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ],
            datetime.date(2022, 2, 2),
            ["duck"]
        )
    ]
)
def test_of_outdated_products(
        products: list,
        date_of_today: datetime,
        outed_product: list
) -> None:
    today = date_of_today
    with mock.patch("datetime.date") as mocked_date:
        mocked_date.today.return_value = today
        assert outdated_products(products) == outed_product
