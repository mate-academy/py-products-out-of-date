import pytest
from unittest import mock
import datetime
from app.main import outdated_products


@pytest.fixture()
def test_outdated_products() -> list:
    outdated = [
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
    return outdated


@mock.patch("app.main.datetime")
def test_outdated_date(
        mocked_date: datetime,
        test_outdated_products: list
) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(test_outdated_products) == ["duck"]
