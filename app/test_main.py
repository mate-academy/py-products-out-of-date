import datetime
import pytest
from unittest import mock

from app.main import outdated_products


@pytest.mark.parametrize("current_date, expected_names", [
    (datetime.date(2022, 2, 2), ["duck"]),
    (datetime.date(2022, 2, 1), []),
    (datetime.date(2022, 2, 6), ["chicken", "duck"]),
])
def test_outdated_products(
        current_date: datetime.date, expected_names: list[str]
) -> None:
    with mock.patch("app.main.datetime") as mocked_datetime:
        mocked_datetime.date.today.return_value = current_date

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
        assert outdated_products(products) == expected_names
