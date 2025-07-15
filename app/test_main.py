import pytest
from unittest import mock
import datetime

from app.main import outdated_products


@pytest.fixture(scope="module")
def products() -> list:
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
    "today,expected",
    [
        (datetime.date(2022, 2, 1), []),
        (datetime.date(2022, 2, 5), ["duck"]),
        (datetime.date(2022, 2, 10), ["chicken", "duck"]),
        (datetime.date(2022, 2, 11), ["chicken", "duck", "salmon"])
    ],
    ids=[
        "no products expired yet",
        "only duck is expired",
        "chicken and duck are expired",
        "all products expired"
    ]
)
@mock.patch("app.main.datetime.date")
def test_outdated_products(
    today_mock: mock.MagicMock,
    today: datetime.date,
    expected: list,
    products: list
) -> None:
    today_mock.today.return_value = today
    assert sorted(outdated_products(products)) == expected
