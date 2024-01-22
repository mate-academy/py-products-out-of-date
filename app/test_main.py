import datetime
import pytest
from app.main import outdated_products
from unittest import mock


products = [
    {
        "name": "salmon",
        "expiration_date": datetime.date(2024, 2, 10),
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
]


@pytest.mark.parametrize(
    "products, expected_today, expected_outdated",
    [(products, datetime.date(2022, 2, 2), ["duck"]),
     (products, datetime.date(2021, 2, 2), []),
     (products, datetime.date(2024, 2, 3), ["chicken", "duck"]),
     ]
)
def test_outdated_products(
    products: list,
    expected_today: type(datetime),
    expected_outdated: list,
) -> list:

    with mock.patch("datetime.date") as mocked_date:
        mocked_date.today.return_value = expected_today

        assert outdated_products(products) == expected_outdated
