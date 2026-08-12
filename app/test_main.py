import pytest
import datetime
from unittest import mock
from typing import Callable


from app.main import outdated_products


@pytest.mark.parametrize(
    "current_date, products, expected_result",
    [
        pytest.param(
            datetime.date(2022, 2, 8),
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
            ["chicken", "duck"],
            id="Should return ['chicken', 'duck'] \
                when only 1 product is not outdated"
        ),
        pytest.param(
            datetime.date(2022, 1, 28),
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
            [],
            id="Should return [] \
                when all products are not outdated"
        ),
        pytest.param(
            datetime.date(2022, 2, 18),
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
            ["salmon", "chicken", "duck"],
            id="Should return ['salmon', 'chicken', 'duck'] \
                when only all products are outdated"
        ),
        pytest.param(
            datetime.date(2022, 2, 2),
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
            ["duck"],
            id="Should return ['duck'] \
                when only 1 product got outdated yesterday"
        ),
        pytest.param(
            datetime.date(2022, 2, 1),
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
            [],
            id="Should return [] \
                when only 1 product will get outdated today"
        )
    ]
)
@mock.patch("datetime.date")
def test_determine_outdated_products_correctly(
    mocked_datetime: Callable,
    current_date: type[datetime.date],
    products: list[dict],
    expected_result: list[str]
) -> None:
    mocked_datetime.today.return_value = current_date
    assert outdated_products(products) == expected_result
