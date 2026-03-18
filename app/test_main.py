from unittest import mock
import pytest
from datetime import date

from app.main import outdated_products


tested_products = [
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
]


@pytest.mark.parametrize("today_date, result_products", [
    (date(2022, 2, 1), []),
    (date(2022, 2, 2), ["duck"]),
    (date(2022, 2, 10), ["chicken", "duck"]),
    (date(2022, 2, 11), ["salmon", "chicken", "duck"])
])
@mock.patch("app.main.datetime")
def test_outdated_products(
        mock_today_date: mock.MagicMock,
        today_date: date,
        result_products: list,
) -> None:
    mock_today_date.date.today.return_value = today_date
    assert outdated_products(tested_products) == result_products
