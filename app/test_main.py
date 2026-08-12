from unittest import mock
from datetime import date
import pytest

from app.main import outdated_products


@pytest.fixture()
def product_cart() -> list:
    return [
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
            "expiration_date": date(2022, 2, 2),
            "price": 160
        }
    ]


@mock.patch("app.main.date")
@pytest.mark.parametrize(
    "today,expected_products",
    [
        pytest.param(date(2022, 2, 11), ["salmon", "chicken", "duck"],
                     id="all products are outdated"),
        pytest.param(date(2022, 2, 10), ["chicken", "duck"],
                     id="salmon exp_date = today"),
        pytest.param(date(2022, 2, 2), [], id="duck exp_date = today"),
        pytest.param(date(2022, 2, 1), [], id="all products are fresh"),
    ]
)
def test_outdated_products_correctly(
        mock_date: callable,
        today: date,
        expected_products: list,
        product_cart: list,
) -> None:
    mock_date.today.return_value = today
    assert outdated_products(product_cart) == expected_products


def test_empty() -> None:
    assert outdated_products([]) == []
