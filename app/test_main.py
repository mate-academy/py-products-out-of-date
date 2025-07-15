import pytest
import datetime
from freezegun import freeze_time
from app.main import outdated_products


@freeze_time("2022-02-03")
@pytest.mark.parametrize(
    "products, expected",
    [
        (
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
            ["duck"]
        ),
        (
            [
                {
                    "name": "ketchup",
                    "expiration_date": datetime.date(2022, 2, 3),
                    "price": 50
                }
            ],
            []
        ),
        (
            [
                {
                    "name": "bread",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 40
                }
            ],
            ["bread"]
        )
    ]
)
def test_outdated_products(
        products: list[dict],
        expected: list[str]
) -> None:
    assert outdated_products(products) == expected
