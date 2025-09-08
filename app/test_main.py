from app.main import outdated_products
import pytest
import datetime


@pytest.mark.parametrize(
    "product, result",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2025, 9, 8),
                    "price": 600
                }
            ],
            []
        ),
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2025, 9, 7),
                    "price": 600
                }
            ],
            ["salmon"]

        )
    ]
)
def test_logic_outdated_products(product: list, result: list) -> None:
    assert outdated_products(product) == result


def test_input_type_error() -> None:
    with pytest.raises(TypeError):
        outdated_products(
            {
                "name": "salmon",
                "expiration_date": datetime.date(2025, 9, 7),
                "price": 600
            }
        )
