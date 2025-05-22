from unittest.mock import MagicMock

from app.main import outdated_products
import pytest
import datetime
from unittest import mock


@pytest.mark.parametrize(
    "product_list, today_date, expected",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600},
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 120},
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                },
            ],
            datetime.date(2022, 2, 2),
            ["duck"],
        ),
    ]
)
@mock.patch("app.main.datetime.date")
def test_should_return_products_out_of_date(mock_date: MagicMock,
                                            product_list: list,
                                            today_date: datetime,
                                            expected: list) -> None:
    mock_date.today.return_value = today_date
    assert outdated_products(product_list) == expected
