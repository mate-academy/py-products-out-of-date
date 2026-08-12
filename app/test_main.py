import pytest
from unittest import mock
from datetime import date
from app.main import outdated_products
from typing import Callable


@pytest.fixture()
def mock_datetime() -> Callable:
    with mock.patch("app.main.datetime.date") as mocked_date:
        yield mocked_date


@pytest.mark.parametrize(
    "input_list",
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
        input_list: list
) -> None:
    mock_datetime.today.return_value = date(2022, 2, 2)
    assert outdated_products(input_list) == ["duck"]
