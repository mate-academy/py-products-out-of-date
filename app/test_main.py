import datetime
from unittest import mock

from app.main import outdated_products

list_for_tests = [
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
        "expiration_date": datetime.date(2022, 2, 3),
        "price": 160
    }]


@mock.patch("app.main.datetime")
def test_when_all_products_are_ok(mocked_dt):
    mocked_dt.date.today.return_value = datetime.date(2022, 2, 2)
    verdict = outdated_products(list_for_tests)
    assert verdict == []


@mock.patch("app.main.datetime")
def test_when_one_products_is_not_ok(mocked_dt):
    mocked_dt.date.today.return_value = datetime.date(2022, 2, 4)
    verdict = outdated_products(list_for_tests)
    assert verdict == ["duck"]


@mock.patch("app.main.datetime")
def test_when_all_products_are_bad(mocked_dt):
    mocked_dt.date.today.return_value = datetime.date(2023, 2, 11)
    verdict = outdated_products(list_for_tests)
    assert verdict == ['salmon', 'chicken', 'duck']
