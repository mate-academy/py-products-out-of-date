import datetime
import pytest

from unittest import mock

from app.main import outdated_products

products_ = [
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
    "products, date, result",
    [
        (products_, datetime.date(2022, 2, 1), []),
        (products_, datetime.date(2022, 2, 2), ["duck"]),
        (products_, datetime.date(2025, 1, 1), ["salmon", "chicken", "duck"])
    ]
)
@mock.patch("datetime.date")
def test_date_expired(mocked_today: mock,
                      products: list[dict],
                      date: datetime,
                      result: list[str]) -> None:
    mocked_today.today.return_value = date
    assert outdated_products(products) == result, \
        f"List should be equal to {result}"
