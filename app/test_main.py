import datetime
import pytest
from unittest import mock
from app.main import outdated_products


products = [
    {
        "name": "salmon",
        "expiration_date": datetime.date(2022, 2, 10),
        "price": 600
    },
    {
        "name": "chicken",
        "expiration_date": datetime.date(2022, 2, 9),
        "price": 120
    },
    {
        "name": "duck",
        "expiration_date": datetime.date(2022, 2, 1),
        "price": 160
    }
]


@pytest.mark.parametrize(
    "today, expected",
    [
        (datetime.date(2022, 2, 9), ["duck"]),
        (
            datetime.date(2022, 2, 11),
            ["salmon", "chicken", "duck"]
        ),
        (datetime.date(2022, 1, 31), []),
    ],
)
@mock.patch("app.main.datetime.date")
def test_outdated_products(
        mocked_date: mock.MagicMock,
        today: datetime.date,
        expected: list
) -> None:
    mocked_date.today.return_value = today
    assert outdated_products(products) == expected
