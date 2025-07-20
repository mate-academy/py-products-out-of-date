import datetime
from unittest.mock import patch, MagicMock
import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "input_data, result",
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
            ["chicken", "duck"]
        )
    ]
)
@patch("app.main.get_today", return_value=datetime.date(2022, 2, 10))
def test_main_func(
        mock_get_today: MagicMock, input_data: list[dict], result: list[str]
) -> None:
    assert outdated_products(input_data) == result
