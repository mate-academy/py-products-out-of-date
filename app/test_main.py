import datetime
from unittest import mock
import pytest

from app.main import outdated_products


@pytest.fixture()
def products_template() -> list:
    return [
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


def test_outdated_products_is_working_correctly(
        products_template: list
) -> None:
    with (mock.patch("app.main.datetime")) as mock_datetime:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 5)
        assert outdated_products(products_template) == ["duck"]

        mock_datetime.date.today.return_value = datetime.date(2024, 2, 5)
        assert outdated_products(products_template) == [
            "salmon", "chicken", "duck"
        ]
