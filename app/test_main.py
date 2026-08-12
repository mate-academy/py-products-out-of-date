import datetime

from unittest import mock

import pytest


from app.main import outdated_products


@pytest.fixture()
def products() -> list[dict]:
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
    "expected, date_time",
    [
        ([], datetime.date(2022, 2, 1)),
        (["chicken", "duck"], datetime.date(2022, 2, 6)),
        (["salmon", "chicken", "duck"], datetime.date(2022, 2, 11)),
    ]
)
def test_outdated_products(
        date_time: datetime,
        products: list[dict],
        expected: list[str]
) -> None:
    with mock.patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = date_time
        assert outdated_products(products) == expected
