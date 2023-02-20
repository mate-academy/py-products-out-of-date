from typing import Callable
from unittest import mock
import pytest
import datetime

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


@pytest.mark.parametrize(
    "today_date, expired_products",
    [
        pytest.param(
            datetime.date(2022, 2, 1), [], id="no expired products"
        ),
        pytest.param(
            datetime.date(2022, 2, 2), ["duck"], id="one expired"
        ),
        pytest.param(
            datetime.date(2022, 2, 6), ["chicken", "duck"], id="2 expired"
        ),
        pytest.param(
            datetime.date(2022, 2, 11),
            ["salmon", "chicken", "duck"],
            id="3 expired products"
        ),
    ]
)
@mock.patch("datetime.date")
def test_list_of_outdated_products(
        mocked_datetime: Callable,
        products_template: list,
        today_date: datetime,
        expired_products: list
) -> None:
    mocked_datetime.today.return_value = today_date
    assert outdated_products(products_template) == expired_products
