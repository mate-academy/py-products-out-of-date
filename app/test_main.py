import datetime
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "date, result", [
        (datetime.date(2022, 2, 2), ["duck"]),
        (datetime.date(2022, 2, 6), ["chicken", "duck"]),
        (datetime.date(2022, 2, 13), ["salmon", "chicken", "duck"])
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(
        out_of_date: mock,
        date: datetime,
        result: list
) -> None:
    out_of_date.date.today.return_value = date
    products: list[dict] = [{
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
    }]
    assert outdated_products(products) == result
