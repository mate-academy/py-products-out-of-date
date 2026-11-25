import pytest
import datetime
from unittest import mock
from app.main import outdated_products

real_time = datetime.date


@pytest.fixture()
def mocked_time() -> mock.MagicMock:
    with mock.patch("app.main.datetime.date") as mocked_time:
        yield mocked_time


def test_datetime_has_been_called(mocked_time: mock.MagicMock) -> None:
    mocked_time.today.return_value = real_time(2026, 11, 25)
    outdated_products(
        [
            {
                "name": "salmon",
                "expiration_date": real_time(2027, 2, 10),
                "price": 600
            }
        ]
    )
    mocked_time.today.assert_called_once()


@pytest.mark.parametrize(
    "products, expected_products",
    (
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": real_time(2027, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": real_time(2026, 11, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": real_time(2026, 11, 25),
                    "price": 160
                }
            ],
            ["chicken"]
        ),
        (
            [
                {
                    "name": "pork",
                    "expiration_date": real_time(2026, 11, 24),
                    "price": 150
                },
                {
                    "name": "apples",
                    "expiration_date": real_time(2026, 11, 26),
                    "price": 50
                },
                {
                    "name": "tomatoes",
                    "expiration_date": real_time(2027, 1, 5),
                    "price": 80
                }
            ],
            ["pork"]
        )
    )
)
def test_func_returns_products_name(
        mocked_time: mock.MagicMock,
        products: list,
        expected_products: list
) -> None:
    mocked_time.today.return_value = real_time(2026, 11, 25)
    assert outdated_products(products) == expected_products
