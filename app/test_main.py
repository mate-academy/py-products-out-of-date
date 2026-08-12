import pytest
from unittest import mock
import datetime
from app.main import outdated_products
from typing import List, Dict


@pytest.mark.parametrize(
    "products, today_date, expected_outdated",
    [
        (
            [
                {"name": "salmon", "expiration_date":
                    datetime.date(2022, 2, 10), "price": 600},
                {"name": "chicken", "expiration_date":
                    datetime.date(2022, 2, 5), "price": 120},
                {"name": "duck", "expiration_date":
                    datetime.date(2022, 2, 1), "price": 160}
            ],
            datetime.date(2022, 2, 6),
            ["chicken", "duck"]
        ),
        (
            [
                {"name": "salmon", "expiration_date":
                    datetime.date(2022, 2, 10), "price": 600},
                {"name": "chicken", "expiration_date":
                    datetime.date(2022, 2, 5), "price": 120},
                {"name": "duck", "expiration_date":
                    datetime.date(2022, 2, 1), "price": 160}
            ],
            datetime.date(2022, 2, 1),
            []
        ),
        (
            [
                {"name": "salmon", "expiration_date":
                    datetime.date(2022, 2, 10), "price": 600},
                {"name": "chicken", "expiration_date":
                    datetime.date(2022, 2, 5), "price": 120},
                {"name": "duck", "expiration_date":
                    datetime.date(2022, 2, 1), "price": 160}
            ],
            datetime.date(2022, 2, 6),
            ["chicken", "duck"]
        )
    ]
)
def test_outdated_products(
    products: List[Dict[str, object]],
    today_date: datetime.date,
    expected_outdated: List[str]
) -> None:
    with mock.patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = today_date
        result = outdated_products(products)
        print(f"Result for {today_date}: {result}")
        assert result == expected_outdated
