import datetime
from unittest import mock
from app.main import outdated_products


@mock.patch("app.main.datetime")
def test_date_is_good(mocked_date):
    product = [{
        "name": "salmon",
        "expiration_date": datetime.date(2022, 8, 29),
        "price": 600
    }]
    mocked_date.date.today.return_value = datetime.date(2022, 8, 29)
    assert outdated_products(product) == []


@mock.patch("app.main.datetime")
def test_expiration_date_is_expired(mocked_date):
    product = [{
        "name": "salmon",
        "expiration_date": datetime.date(2022, 8, 28),
        "price": 600
    }]
    mocked_date.date.today.return_value = datetime.date(2022, 8, 29)
    assert outdated_products(product) == ["salmon"]
