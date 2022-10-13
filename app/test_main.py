import datetime
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.fixture()
def mock_date() -> None:
    with mock.patch("app.main.datetime.date") as mock_date:
        yield mock_date


def test_product(mock_date: mock) -> None:
    mock_date.return_value = datetime.date(2022, 2, 1)
    assert outdated_products([
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
    ]) == ["duck"]
