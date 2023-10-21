from unittest import mock
from unittest.mock import MagicMock
import pytest
from app.main import outdated_products
import datetime


@mock.patch("datetime.date")
@pytest.mark.parametrize(
    "product_data, result",
    [
        (
            [
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
            ],
            ["duck"]
        )
    ]
)
def test_outdated_products(mocked_datetime_date_today: MagicMock,
                           product_data: list[dict],
                           result: list) -> None:

    today_date = datetime.datetime(2022, 2, 5)
    mocked_datetime_date_today.today.return_value = today_date.date()
    assert outdated_products(product_data) == result


@mock.patch("datetime.date")
@pytest.mark.parametrize(
    "product_data, result",
    [
        (
            [
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
            ],
            ["duck"]
        )
    ]
)
def test_expiration_day_yesterday_outdated(
        mocked_datetime_date_today: MagicMock,
        product_data: list[dict],
        result: list) -> None:

    today_date = datetime.datetime(2022, 2, 2)
    mocked_datetime_date_today.today.return_value = today_date.date()
    assert outdated_products(product_data) == result
