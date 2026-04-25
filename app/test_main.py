import pytest
import datetime
from unittest.mock import patch, MagicMock
from app.main import outdated_products


@pytest.mark.parametrize(
    "today_date, list_of_products, expected_result",
    [
        (
            datetime.date(2026, 4, 25),
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
                }
            ],
            ["salmon", "chicken"]
        ),
        (
            datetime.date(2022, 2, 4),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 3),
                    "price": 120
                }
            ],
            ["chicken"]
        ),

    ]
)
@patch("app.main.datetime")
def test_outdated_products_logic(
    mocked_datetime: MagicMock,
    today_date: datetime.date,
    list_of_products: list,
    expected_result: list
) -> None:
    mock_today = mocked_datetime.date.today
    mock_today.return_value = today_date
    assert outdated_products(list_of_products) == expected_result
