from unittest.mock import patch, Mock
from datetime import date

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "actual, date_today, expected",
    [
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": date(2022, 2, 1),
                    "price": 160
                }
            ],
            date.today(),
            ["salmon", "chicken", "duck"],
            id="test should pass if all food is outdated"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": date(2022, 2, 1),
                    "price": 160
                }
            ],
            date(2022, 2, 10),
            ["chicken", "duck"],
            id="test should pass if today is last day of expiration"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": date(2022, 2, 1),
                    "price": 160
                }
            ],
            date(2022, 2, 11),
            ["salmon", "chicken", "duck"],
            id="test should pass if yesterday was a last day of expiration"
        ),
    ]
)
@patch("app.main.datetime")
def test_should_return_correct_list(
        mocked_time,
        actual,
        date_today,
        expected
):
    mocked_time.date.today = Mock(
        return_value=date_today
    )
    assert outdated_products(actual) == expected
