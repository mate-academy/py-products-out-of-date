import datetime
import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "products, expected_result",
    [
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2024, 2, 20),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2024, 2, 18),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2024, 2, 17),
                    "price": 160
                }
            ],
            ["duck"],
            id="should return list with outdated products names"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2024, 2, 20),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2024, 2, 18),
                    "price": 120
                },
            ],
            [],
            id="should return empty list if no outdated products"
        )
    ]
)
def test_outdated_products(products: list, expected_result: list) -> None:
    result = outdated_products(products)

    assert result == expected_result
