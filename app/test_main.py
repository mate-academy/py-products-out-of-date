from _datetime import datetime
from unittest import mock
import pytest

from .main import outdated_products


@pytest.mark.parametrize(
    "today_date,expected",
    (
            [datetime(2022, 1, 10), []],
            [datetime(2022, 1, 11), ["duck"]],
            [datetime(2022, 2, 5), ["chicken", "duck"]],
            [datetime(2022, 2, 24), ["salmon", "chicken", "duck"]],
    )
)
def test_outdated_products(
        today_date: datetime.date,
        expected: list
) -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime(2022, 2, 22),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime(2022, 2, 1),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime(2022, 1, 10),
            "price": 160
        }
    ]
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = today_date
        assert outdated_products(products) == expected
