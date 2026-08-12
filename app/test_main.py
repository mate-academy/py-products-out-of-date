import datetime
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.mark.parametrize("date, users, expected", [
    (datetime.date(2020, 1, 1), [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600,

        }], []),
    (datetime.date(2023, 1, 1), [
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120,
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ], ["chicken", "duck"]),
    (datetime.date.today(), [
        {
            "name": "salmon",
            "expiration_date": datetime.date.today(),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date":
                datetime.date.today() - datetime.timedelta(days=1),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ], ["chicken", "duck"])

])
@mock.patch("app.main.datetime.date")
def test_outdated_products(mock_data: mock.MagicMock,
                           date: datetime,
                           users: list[dict],
                           expected: list) -> None:
    mock_data.today.return_value = date
    assert outdated_products(users) == expected
