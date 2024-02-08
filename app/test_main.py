import datetime
import pytest
from unittest.mock import patch
from app.main import outdated_products


@pytest.fixture()
def list_of_products() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 12, 31),
            "price": 120
        },
        {
            "name": "apples",
            "expiration_date": datetime.date(2023, 1, 1),
            "price": 120
        }
    ]


@pytest.mark.parametrize(
    "today_date, expected",
    [
        (datetime.date(2023, 1, 1), ["salmon", "chicken"]),
    ]
)
@patch("app.main.datetime")
def test_outdated_products(
        mock_datetime: callable,
        list_of_products: list,
        today_date: datetime.date,
        expected: list[str]
) -> None:
    mock_datetime.date.today.return_value = today_date

    assert outdated_products(list_of_products) == expected
