from datetime import date
from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import outdated_products


@pytest.fixture()
def mocked_today() -> MagicMock:
    with mock.patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = date(2022, 2, 2)
        mock_date.side_effect = lambda *args, **kw: date(*args, **kw)
        yield mock_date


def test_outdated_products(mocked_today: mock) -> None:
    test_products = [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 3),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 2),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        }
    ]
    assert outdated_products(test_products) == ["duck"]
