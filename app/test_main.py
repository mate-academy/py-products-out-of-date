import pytest
import datetime
from unittest import mock
from typing import Any
from .main import outdated_products


@pytest.mark.parametrize(
    "mocked_today, products, expected_result",
    [
        (
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 600},
                {
                    "name": "cheese",
                    "expiration_date": datetime.date(2022, 2, 3),
                    "price": 300
                },
            ],
            ["salmon"],
        ),
        (
            datetime.date(2022, 2, 5),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 4),
                    "price": 160
                },
            ],
            ["salmon", "duck"],
        ),
        (
            datetime.date(2022, 2, 1),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 1, 31),
                    "price": 600
                },
                {
                    "name": "cheese",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 300
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 120
                },
            ],
            ["salmon"],
        ),
    ],
    ids=[
        "date_is_2_feb_2022",
        "date_is_5_feb_2022",
        "date_is_1_feb_2022",
    ]
)
def test_outdated_products(
        mocked_today: datetime.date,
        products: list[dict[str, Any]],
        expected_result: list[str],
) -> None:
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = mocked_today

        result = outdated_products(products)

    assert result == expected_result,\
        f"Expected {expected_result}, but got {result}"
