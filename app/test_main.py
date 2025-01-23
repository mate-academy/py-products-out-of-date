import datetime

from app.main import outdated_products
import pytest
from unittest import mock


@pytest.mark.parametrize(
    "products,today,result",
    [
        (
            [
                {"name": "salmon",
                 "expiration_date": datetime.date(2022, 2, 10)},
                {"name": "chicken",
                 "expiration_date": datetime.date(2025, 2, 10)},
                {"name": "duck",
                 "expiration_date": datetime.date(2023, 5, 19)},
            ],
            "2025 01 23",
            ["salmon", "duck"],
        ),
        (
            [
                {"name": "salmon",
                 "expiration_date": datetime.date(2022, 2, 10)},
                {"name": "chicken",
                 "expiration_date": datetime.date(2025, 2, 10)},
                {"name": "duck",
                 "expiration_date": datetime.date(2023, 5, 19)},
            ],
            "2022 10 12",
            ["salmon"],
        )
    ],
    ids=[
        "test when 2 of 3 are expired products",
        "test when 1 of 3 are expired products",
    ]
)
def test_outdated_products(
        products: list, today: str, result: list
) -> None:
    with mock.patch("app.main.datetime") as mocked_date:
        year, month, day = today.split()
        mocked_date.date.today.return_value = datetime.date(
            int(year), int(month), int(day)
        )
        assert outdated_products(products) == result
