import datetime
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.fixture()
def products_template() -> list[dict]:
    products = [
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
    ]
    return products


@pytest.mark.parametrize(
    "today_date,result",
    [
        (
            datetime.date(2022, 2, 2),
            ["duck"]
        ),
        (
            datetime.date(2022, 2, 10),
            ["chicken", "duck"]
        ),
        (
            datetime.date(2022, 2, 12),
            ["salmon", "chicken", "duck"]
        )
    ]
)
def test_outdated_products(
        products_template: list[dict], today_date: datetime.date, result: list
) -> None:
    with mock.patch("datetime.date") as mock_today:
        mock_today.today.return_value = today_date
        assert outdated_products(products_template) == result
