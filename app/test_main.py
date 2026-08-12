from unittest.mock import MagicMock
from unittest import mock
from typing import List, Dict, Any
import datetime
import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "mocked_today, products, expected",
    [
        (
            datetime.date(2022, 2, 2),
            [
                {"name": "salmon",
                 "expiration_date": datetime.date(2022, 2, 10),
                 "price": 600},
                {"name": "chicken",
                 "expiration_date": datetime.date(2022, 2, 5),
                 "price": 120},
                {"name": "duck", "expiration_date": datetime.date(2022, 2, 1),
                 "price": 160},
            ],
            ["duck"]
        ),
        (
            datetime.date(2022, 10, 2),
            [
                {"name": "salmon",
                 "expiration_date": datetime.date(2022, 2, 10),
                 "price": 600},
                {"name": "chicken",
                 "expiration_date": datetime.date(2022, 2, 5),
                 "price": 120},
                {"name": "duck",
                 "expiration_date": datetime.date(2022, 2, 1),
                 "price": 160},
            ],
            ["salmon", "chicken", "duck"]
        ),
        (
            datetime.date(2022, 2, 2),
            [{"name": "fresh_fish",
              "expiration_date": datetime.date(2022, 2, 2)}],
            []
        ),
    ]
)
@mock.patch("app.main.datetime.date")
def test_outdated_products(
    mock_date: MagicMock,
    mocked_today: datetime.date,
    products: List[Dict[str, Any]],
    expected: List[str]
) -> None:
    mock_date.today.return_value = mocked_today
    result = outdated_products(products)
    assert result == expected
