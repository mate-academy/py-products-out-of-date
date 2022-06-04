import datetime
from freezegun import freeze_time

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "products,exception",
    [
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 6, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 6, 15),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 6, 3),
                    "price": 160
                },
            ],
            ["duck"],
            id="Check normal work"),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date.today(),
                    "price": 600
                }
            ],
            [],
            id="Check date == today",
        )
    ]
)
@freeze_time(f"{datetime.date.today()}")
def test_outdated_product(products, exception):
    assert outdated_products(products) == exception
