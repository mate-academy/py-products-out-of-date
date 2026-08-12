import pytest
import datetime
from app.main import outdated_products


@pytest.mark.parametrize(
    "list_of_products, result",
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
                    "expiration_date": datetime.date(2026, 2, 5),
                    "price": 120
                }
            ], ["salmon"], id="one_products"),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date.today(),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2026, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2025, 1, 13),
                    "price": 160
                }
            ],
            ["duck"], id="two_products"),
    ]
)
def test_outdated_products(list_of_products: list, result: list) -> None:
    res = outdated_products(list_of_products)
    assert res == result
