from __future__ import annotations

import datetime
from typing import List, Dict, Any
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "products, today, expected",
    [
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                },
            ],
            datetime.date(2022, 2, 2),
            ["duck"],
            id="one outdated"
        ),
        pytest.param(
            [
                {
                    "name": "milk",
                    "expiration_date": datetime.date(2022, 1, 1),
                    "price": 50
                },
                {
                    "name": "bread",
                    "expiration_date": datetime.date(2022, 1, 2),
                    "price": 30
                },
            ],
            datetime.date(2022, 2, 2),
            ["milk", "bread"],
            id="all outdated"
        ),
        pytest.param(
            [
                {
                    "name": "cheese",
                    "expiration_date": datetime.date(2022, 2, 3),
                    "price": 200
                },
                {
                    "name": "ham",
                    "expiration_date": datetime.date(2022, 2, 4),
                    "price": 180
                },
            ],
            datetime.date(2022, 2, 2),
            [],
            id="none outdated"
        ),
        pytest.param(
            [
                {
                    "name": "yogurt",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 40
                },
            ],
            datetime.date(2022, 2, 2),
            [],
            id="boundary equal today"
        ),
        pytest.param(
            [],
            datetime.date(2022, 2, 2),
            [],
            id="empty list"
        ),
    ],
)
@mock.patch("app.main.datetime.date")
def test_outdated_products(
    mock_date: mock.MagicMock,
    products: List[Dict[str, Any]],
    today: datetime.date,
    expected: List[str],
) -> None:

    mock_date.today.return_value = today

    mock_date.side_effect = lambda *args, **kwargs: (
        datetime.date(*args, **kwargs))

    result = outdated_products(products)

    assert result == expected
