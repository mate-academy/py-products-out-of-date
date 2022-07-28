from unittest import mock

import datetime

from app.main import outdated_products


products = [{"name": "salmon",
             "expiration_date": datetime.date(2022, 7, 9),
             "price": 600}]


@mock.patch("app.main.datetime")
def test_out_date(mocked_date):
    mocked_date.date.today.return_value = datetime.date(2022, 7, 10)
    assert outdated_products(products) == ["salmon"]


@mock.patch("app.main.datetime")
def test_in_date(mocked_date):
    mocked_date.date.today.return_value = datetime.date(2022, 7, 9)
    assert outdated_products(products) == []
