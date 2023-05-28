import app.main
from app.main import outdated_products
import pytest
import datetime
from unittest.mock import patch
from typing import Callable


def test_input_value() -> None:
    with pytest.raises(TypeError):
        outdated_products(":)")


def test_return_value() -> None:
    assert isinstance(outdated_products({}), list)


@pytest.fixture()
def products_template() -> list:
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
    "mock_datetime_today, result",
    [
        (datetime.date(2022, 2, 1), []),
        (datetime.date(2022, 2, 2), ["duck"]),
        (datetime.date(2022, 2, 6), ["chicken", "duck"]),
        (datetime.date(2022, 2, 11), ["salmon", "chicken", "duck"])
    ]
)
@patch("datetime.date")
def test_outdated_products(mock_datetime,
                           mock_datetime_today: tuple,
                           result: list,
                           products_template: list) -> None:
    mock_datetime.today.return_value = mock_datetime_today
    assert app.main.outdated_products(products_template) == result
