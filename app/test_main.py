from datetime import date, timedelta

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "products, expected",
    [
        pytest.param(
            [
                {
                    "name": "product1",
                    "expiration_date": date(1, 1, 1),
                    "price": 1
                },
                {
                    "name": "product2",
                    "expiration_date": date(1, 1, 1),
                    "price": 1
                }
            ],
            ["product1", "product2"]
        ),
        pytest.param(
            [
                {
                    "name": "product1",
                    "expiration_date": date.today() - timedelta(days=1),
                    "price": 1
                }
            ],
            ["product1"]
        ),
        pytest.param(
            [
                {
                    "name": "product1",
                    "expiration_date": date.today(),
                    "price": 1
                }
            ],
            []
        )
    ]
)
def test_outdated_products(products: list[dict],
                           expected: list[dict]
                           ) -> None:
    assert outdated_products(products) == expected
