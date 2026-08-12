from datetime import date
from typing import Callable
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.fixture()
def mock_datetime() -> Callable:
    with mock.patch("app.main.datetime.date") as mocked_date:
        yield mocked_date


@pytest.mark.parametrize(
    "diccc",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": date(2022, 2, 10),
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
        )
    ]
)
def test_should_return_correct_dict(
        mock_datetime: Callable,
        diccc: dict
) -> None:
    mock_datetime.today.return_value = date(2022, 2, 2)
    assert outdated_products(diccc) == ["duck"]
