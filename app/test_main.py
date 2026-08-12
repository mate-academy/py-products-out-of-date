import pytest
from typing import Callable
from unittest import mock
import datetime
from app.main import outdated_products


@pytest.fixture()
def mocked_datetime() -> None:
    with mock.patch("app.main.datetime") as mock_datetime:
        yield mock_datetime


@pytest.mark.parametrize(
    "product, result",
    [
        ([{
            "name": "salmon",
            "expiration_date": datetime.date.today(),
            "price": 600
        }], []),
        ([{
            "name": "salmon",
            "expiration_date": datetime.date(2023, 1, 31),
            "price": 600
        }], ["salmon"]),
    ]
)
def test_cryptocurrency_action_result(
        mocked_datetime: Callable,
        product: dict,
        result: bool
) -> None:
    mocked_datetime.date.today.return_value = datetime.date.today()
    assert outdated_products(product) == result
