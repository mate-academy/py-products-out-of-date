import pytest
import datetime
from unittest import mock
from app.main import outdated_products


@pytest.mark.parametrize(
    "products,date,expected",
    [
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2025, 4, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2025, 4, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2025, 2, 1),
                    "price": 160
                }
            ],
            datetime.date(2025, 3, 26),
            ["duck"],
            id="if one of products is out of date"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2023, 10, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2023, 2, 4),
                    "price": 120
                }
            ],
            datetime.date(2023, 2, 4),
            [],
            id="if all products are fresh"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2024, 4, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2025, 6, 4),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2025, 6, 4),
                    "price": 160
                }
            ],
            datetime.date(2025, 6, 5),
            ["salmon", "chicken", "duck"],
            id="if all products are out of date"
        ),
        pytest.param(
            [],
            datetime.date(2025, 6, 5),
            [],
            id="if list of products is empty"
        )
    ]
)
def test_of_outdated_products_function(products: list[dict],
                                       date: datetime,
                                       expected: list) -> None:
    with mock.patch("datetime.date") as mocked_date:
        mocked_date.today.return_value = date
        assert outdated_products(products) == expected
