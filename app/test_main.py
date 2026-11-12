import datetime
from unittest import mock
import pytest
from app.main import outdated_products


@pytest.mark.parametrize(
    "product,today_date,expected",
    [
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2026, 11, 11),
                    "price": 600
                },
            ],
            datetime.date(2026, 11, 12),
            ["salmon"],
            id="One outdated product"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2025, 12, 1),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2025, 5, 11),
                    "price": 120
                },
            ],
            datetime.date(2026, 11, 12),
            ["salmon", "chicken"],
            id="Two outdated products"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2025, 12, 1),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2025, 5, 11),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 4, 21),
                    "price": 160
                },
            ],
            datetime.date(2026, 11, 12),
            ["salmon", "chicken", "duck"],
            id="Three outdated products"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2027, 12, 1),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2026, 11, 13),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2028, 8, 15),
                    "price": 160
                },
            ],
            datetime.date(2026, 11, 12),
            [],
            id="Not a single outdated product"
        ),
        pytest.param(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2026, 11, 12),
                    "price": 600
                },
            ],
            datetime.date(2026, 11, 12),
            [],
            id="Today's date is not expired"
        ),
    ],
)
@mock.patch("datetime.date")
def test_outdated_products(
        mocked_date: datetime.date,
        product: list[dict],
        today_date: datetime.date,
        expected: list,
) -> None:
    mocked_date.today.return_value = today_date
    assert outdated_products(product) == expected
