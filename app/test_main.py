import pytest

import datetime
from unittest.mock import patch
from typing import List

from app.main import outdated_products


@pytest.fixture()
def products_data() -> List[dict]:
    yield [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120,
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160,
        },
    ]


@pytest.mark.parametrize(
    "today, expected_list",
    [
        pytest.param(datetime.date(2022, 1, 1), [], id="not outdated"),
        pytest.param(datetime.date(2022, 2, 1), [], id="day of excpiration"),
        pytest.param(
            datetime.date(2022, 3, 3),
            ["salmon", "chicken", "duck"],
            id="outdated",
        ),
    ],
)
def test_outdated_products(
    today: datetime.date.today,
    expected_list: List[str],
    products_data: List[dict],
) -> None:
    with patch("app.main.datetime") as mocked_today:
        mocked_today.date.today.return_value = today
        assert outdated_products(products_data) == expected_list
