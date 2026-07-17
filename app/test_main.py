import datetime
import pytest


from app.main import outdated_products


@pytest.mark.parametrize(
    "products, expected",
    [
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date":
                        datetime.date.today() - datetime.timedelta(days=1),
                    "price": 600
                }
            ],
            ["salmon"],
            id="if the product is expired"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date.today(),
                    "price": 600
                }
            ],
            [],
            id="if the expiration date is today"
        )
    ]
)
def test_outdated_products(products: list, expected: list) -> None:
    assert outdated_products(products) == expected
