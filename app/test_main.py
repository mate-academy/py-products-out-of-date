import datetime
from unittest import mock
from app.main import outdated_products

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


@mock.patch("app.main.datetime")
def test_every_product_is_fresh(mocked_today):
    mocked_today.date.today.return_value = datetime.date(2022, 1, 1)
    assert outdated_products(products) == []


@mock.patch("app.main.datetime")
def test_every_product_is_outdated(mocked_today):
    mocked_today.date.today.return_value = datetime.date(2022, 3, 1)
    assert outdated_products(products) == ["salmon", "chicken", "duck"]


@mock.patch("app.main.datetime")
def test_outdate_equal_exp_day(mocked_today):
    for product in products:
        mocked_today.date.today.return_value = product["expiration_date"]
    assert outdated_products(products) == []
