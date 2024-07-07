import pytest
from unittest import mock
import datetime

from app.main import outdated_products


@pytest.mark.parametrize(
    "products_list, outdated_list",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600,
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120,
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160,
                },
            ],
            ["duck"],
        )
    ],
)
def test_is_the_expiration_date_being_checked_correctly(
    products_list: list[dict], outdated_list: list
) -> None:
    with mock.patch("app.main.datetime") as mock_date:
        mock_date.date.today.return_value = datetime.date(2022, 2, 2)
        assert outdated_products(products_list) == outdated_list
