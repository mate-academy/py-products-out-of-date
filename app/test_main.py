import pytest
import datetime
from unittest.mock import patch, MagicMock
from app.main import outdated_products


@pytest.mark.parametrize(
    "initial_value,expected_result",
    [
        (
            [
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
            ],
            [
                "duck"
            ]
        )
    ]
)
@patch("app.main.datetime")
def test_main(
    mock_today: MagicMock,
    initial_value: list,
    expected_result: list
) -> None:
    mock_today.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(initial_value) == expected_result
