import datetime
from unittest.mock import patch, MagicMock

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "today_date, products, expected",
    [
        (
            datetime.date(2022, 2, 2),
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600,
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160,
                },
            ],
            ["duck"],
        ),
        (
            datetime.date(2022, 2, 5),
            [
                {
                    "name": "expires_today",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 100,
                },
            ],
            [],
        ),
    ]
)
@patch("app.main.datetime.date")
def test_outdated_products(
    mock_date: MagicMock,
    today_date: datetime.date,
    products: list[dict],
    expected: list[str]
) -> None:
    mock_date.today.return_value = today_date
    mock_date.side_effect = lambda *args: datetime.date(*args)

    result = outdated_products(products)
    assert result == expected
