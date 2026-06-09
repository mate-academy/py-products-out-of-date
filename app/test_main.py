import datetime
from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import outdated_products


@pytest.fixture
def products() -> list[dict]:
    return [
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


@pytest.mark.parametrize(
    "today_date,expired_products",
    [
        (datetime.date(2022, 1, 2), []),
        (datetime.date(2022, 2, 2), ["duck"]),
        (datetime.date(2022, 2, 7), ["chicken", "duck"]),
        (datetime.date(2022, 2, 10), ["chicken", "duck"]),
        (datetime.date(2022, 3, 2), ["salmon", "chicken", "duck"]),
    ])
@mock.patch("datetime.date", wraps=datetime.date)
def test_outdated_products(
        mock_date: MagicMock,
        products: list[dict],
        today_date: datetime.date,
        expired_products: list[str]
) -> None:
    mock_date.today.return_value = today_date
    assert outdated_products(products) == expired_products
