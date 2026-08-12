import datetime
import pytest

from unittest import mock

from app.main import outdated_products


products_to_check = [
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
    "products, expire_date, expected_result",
    [
        (products_to_check, datetime.date(2022, 2, 1), []),
        (products_to_check, datetime.date(2022, 2, 2), ["duck"]),
        (
            products_to_check,
            datetime.date(2025, 1, 1),
            ["salmon", "chicken", "duck"]
        )
    ],
    ids=[
        "Empty list testing",
        "'duck' is expired",
        "'salmon, chicken, duck' are expired"
    ]
)
@mock.patch("datetime.date")
def test_date_expired(mocked_today: mock,
                      products: list[dict],
                      expire_date: datetime,
                      expected_result: list[str]) -> None:
    mocked_today.today.return_value = expire_date

    assert outdated_products(products) == expected_result
