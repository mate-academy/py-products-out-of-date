import datetime

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "products,result",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date.today(),
                    "price": 600,
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(
                        datetime.date.today().year,
                        datetime.date.today().month,
                        datetime.date.today().day - 1,
                    ),
                    "price": 120,
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160,
                },
            ],
            ["chicken", "duck"],
        ),
    ],
)
def test_outdated_function(products: list, result: list[str]) -> None:
    assert outdated_products(products) == result
    # ['duck']
