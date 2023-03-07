import datetime
import pytest

from unittest import mock

from app.main import outdated_products

products_info = [
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
    "products, date_today, result",
    [
        (products_info, datetime.date(2022, 2, 1), []),
        (products_info, datetime.date(2022, 2, 2), ["duck"]),
        (
            products_info,
            datetime.date(2023, 1, 1),
            ["salmon", "chicken", "duck"]
        )
    ]
)
@mock.patch("datetime.date")
def test_date_expired(mocked_today: mock,
                      products: list[dict],
                      date_today: datetime,
                      result: list[str]) -> None:
    mocked_today.today.return_value = date_today
    assert outdated_products(products) == result
