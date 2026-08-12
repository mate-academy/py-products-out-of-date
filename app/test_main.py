import pytest
from unittest import mock
import datetime

from app.main import outdated_products


@pytest.fixture()
def test_products() -> list[dict]:
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
    "today_, result",
    [
        (datetime.date(2022, 2, 2), ["duck"]),
        (datetime.date(2022, 2, 6), ["chicken", "duck"]),
        (datetime.date(2022, 2, 11),
         ["salmon", "chicken", "duck"]),
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(mock_today: object,
                           test_products: list[dict],
                           today_: object, result: list[str]) -> None:
    mock_today.date.today.return_value = today_
    assert outdated_products(test_products) == result
