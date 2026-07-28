import datetime
import pytest

from unittest.mock import MagicMock
from unittest import mock

from app.main import outdated_products


@pytest.mark.parametrize(
    "products_list,expected,year,month,day",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(
                        2026, 7, 26
                    ),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(
                        2026, 7, 27
                    ),
                    "price": 120
                }
            ],
            ["salmon"],
            2026, 7, 27
        ),
        (
            [
                {
                    "name": "duck",
                    "expiration_date": datetime.date(
                        2026, 7, 29
                    ),
                    "price": 160
                },
            ],
            [],
            2026, 7, 28
        ),
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(
        mock_datetime: MagicMock,
        products_list: list[dict],
        expected: list,
        year: int,
        month: int,
        day: int
) -> None:
    mock_datetime.date.today.return_value = datetime.date(year, month, day)
    assert outdated_products(products_list) == expected

    mock_datetime.date.today.assert_called()
