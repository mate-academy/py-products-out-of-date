from datetime import date

from unittest import mock
import pytest

from app.main import outdated_products


@pytest.fixture
def product_list() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 5),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 2),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        }
    ]


def test_yesterday_outdated_product(
        product_list: list
) -> None:
    with mock.patch("app.main.datetime.date") as mock_datetime:
        mock_datetime.today.return_value = date(2022, 2, 2)
        assert (
            outdated_products(product_list) == ["duck"]
        ), "Product with expiration date equals yesterday is outdated."


def test_today_product(
        product_list: list
) -> None:
    with mock.patch("app.main.datetime.date") as mock_datetime:
        mock_datetime.today.return_value = date(2022, 2, 1)
        assert (
            outdated_products(product_list) == []
        ), "Product with expiration date equals today is not outdated."
