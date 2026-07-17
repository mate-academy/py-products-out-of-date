import datetime
from typing import Any, Generator
from unittest import mock
from unittest.mock import MagicMock, AsyncMock

import pytest

from app.main import outdated_products


products = [
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
]


@pytest.fixture
def mock_today_date() -> Generator[MagicMock | AsyncMock, Any, None]:
    with mock.patch(
            "app.main.datetime.date",
    ) as mock_today_date:
        yield mock_today_date


@pytest.mark.parametrize(
    "today_date, expected_outdated_products",
    [
        pytest.param(
            datetime.date(2022, 2, 20),
            ["salmon", "chicken", "duck"],
            id="all products outdated"
        ),
        pytest.param(
            datetime.date(2022, 2, 1),
            [],
            id="expiration day is today - not outdated"
        ),
        pytest.param(
            datetime.date(2022, 2, 2),
            ["duck"],
            id="one product outdated"
        ),
        pytest.param(
            datetime.date(2022, 1, 30),
            [],
            id="none of products outdated"
        ),
    ]
)
def test_return_outdated_products_correctly(
        today_date: datetime.date,
        expected_outdated_products: list,
        mock_today_date: MagicMock | AsyncMock
) -> None:
    mock_today_date.today.return_value = today_date
    assert outdated_products(products) == expected_outdated_products
