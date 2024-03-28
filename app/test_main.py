import pytest
import datetime
from unittest import mock

from app.main import outdated_products

product_template = [
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
    "current_date, expected_res",
    [
        (datetime.date(2022, 1, 25), []),
        (datetime.date(2022, 2, 4), ["duck"]),
        (datetime.date(2022, 2, 6), ["chicken", "duck"]),
        (datetime.date(2022, 2, 15), ["salmon", "chicken", "duck"])
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_product(
        mocked_today: mock.MagicMock,
        current_date: datetime,
        expected_res: list
) -> None:
    mocked_today.date.today.return_value = current_date
    assert outdated_products(product_template) == expected_res
