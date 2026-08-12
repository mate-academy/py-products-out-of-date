import pytest
import datetime
from unittest import mock
from app.main import outdated_products


@pytest.fixture()
def test_date_out() -> list:
    products = [
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
    return products


@mock.patch("app.main.datetime")
def test_out_date(mocked_time: mock, test_date_out: mock) -> None:
    mocked_time.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products=test_date_out) == ["duck"]
