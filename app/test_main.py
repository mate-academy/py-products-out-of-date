from unittest import mock
import datetime
import pytest
from app.main import outdated_products


@pytest.mark.parametrize(
    "dict_product, expected_product",
    [
        (
            [{
                "name": "duck",
                "expiration_date": datetime.date(2024, 4, 4),
                "price": 160
            }],
            []
        ),
        (
            [{
                "name": "salmon",
                "expiration_date": datetime.date(2024, 4, 5),
                "price": 160
            }],
            []
        ),
        (
            [{
                "name": "chicken",
                "expiration_date": datetime.date(2024, 4, 3),
                "price": 120
            }],
            ["chicken"]
        )
    ]
)
def test_outdated_products(
        dict_product: list,
        expected_product: str
) -> None:
    with mock.patch("app.main.datetime") as mocked_date:
        mocked_date.date.today.return_value = datetime.date(2024, 4, 4)
        assert outdated_products(dict_product) == expected_product
