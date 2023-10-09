from datetime import date
from unittest import mock
import pytest
from app.main import outdated_products


@pytest.fixture()
def mocked_datetime() -> None:
    with mock.patch("datetime.date") as mocked_date:
        yield mocked_date


def test_expiration_day_yesterday_outdated(mocked_datetime: callable) -> None:
    mocked_datetime.today.return_value = date(2023, 10, 9)
    product_list = [
        {
            "name": "salmon",
            "expiration_date": date(2023, 10, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2023, 10, 8),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2023, 10, 9),
            "price": 160
        }
    ]
    assert outdated_products(product_list) == ["chicken"]
