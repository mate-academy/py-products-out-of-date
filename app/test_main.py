import datetime
from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import outdated_products

#  capture the real date class BEFORE any patching
real_date = datetime.date


@pytest.fixture
def sample_products_list() -> list[dict]:
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
            "name": "soup",
            "expiration_date": datetime.date(2022, 2, 4),
            "price": 99
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]


@mock.patch("app.main.datetime.date")
def test_outdated_products(
        mock_date: MagicMock,
        sample_products_list: list[dict]
) -> None:
    # Use the original class so constructions produce real datetime.date
    mock_date.side_effect = real_date

    # Make today() return a real datetime.date
    mock_date.today.return_value = real_date(2022, 2, 5)
    assert outdated_products(sample_products_list) == ["soup", "duck"]
