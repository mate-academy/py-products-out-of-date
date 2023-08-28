from unittest import mock
import datetime

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "date1,date2,expected_result",
    [
        pytest.param(
            datetime.date(2023, 8, 14),
            datetime.date(2023, 9, 15),
            ["salmon"],
            id="should return only spoiled products"
        ),
        pytest.param(
            datetime.date(2023, 8, 14),
            datetime.date(2023, 8, 14),
            ["salmon", "chicken"],
            id="should return all spoiled products"
        ),
        pytest.param(
            datetime.date(2023, 8, 16),
            datetime.date(2023, 8, 16),
            [],
            id="should return an empty lists if no spoiled products"
        )
    ]
)
def test_should_check_products_correctly(
        date1: datetime,
        date2: datetime,
        expected_result: list
) -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": date1,
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date2,
            "price": 120
        }
    ]
    with mock.patch("app.main.datetime") as mocked_date:
        mocked_date.date.today.return_value = datetime.date(2023, 8, 15)
        assert outdated_products(products) == expected_result
