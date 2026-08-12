import datetime
from unittest import mock
import pytest
from app.main import outdated_products


@pytest.mark.parametrize(
    "today, products, expected",
    [
        (datetime.date(2025, 1, 1), [], []),
        (datetime.date(2025, 1, 3), [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2025, 1, 2),
                "price": 600,
            }
        ], ["salmon"], ),
        (datetime.date(2025, 1, 3), [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2025, 1, 2),
                "price": 600,
            }
        ], ["salmon"], ),
        (datetime.date(2025, 1, 3), [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2025, 1, 3),
                "price": 600,
            }
        ], [],),
        (datetime.date(2025, 1, 3), [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2025, 1, 2),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2025, 1, 2),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2025, 1, 2),
                "price": 160
            }
        ], ["salmon", "chicken", "duck"], ),
        (datetime.date(2025, 1, 1), [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2025, 1, 2),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2025, 1, 2),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2025, 1, 2),
                "price": 160
            }
        ], [], ),
        (datetime.date(2025, 1, 2), [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2025, 1, 3),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2025, 1, 1),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2025, 1, 3),
                "price": 160
            }
        ], ["chicken"], ),
        (datetime.date(2025, 1, 2), [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2025, 1, 1),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2025, 1, 3),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2025, 1, 1),
                "price": 160
            }
        ], ["salmon", "duck"], )

    ],
    ids=[
        "empty products list",
        "salmon not expired",
        "salmon is expired",
        "expiration date equals today",
        "all products not expired",
        "all products is expired",
        "one product not expired",
        "one product is expired",
    ],
)
def test_outdated_products(
        today: datetime, products: list, expected: list
) -> None:
    with mock.patch("datetime.date") as mocked_date:
        mocked_date.today.return_value = today
        assert outdated_products(products) == expected
