import datetime
import pytest
from unittest import mock
from app.main import outdated_products

products = [
    {"name": "salmon",  "expiration_date": datetime.date(2022, 2, 10), "price": 600},
    {"name": "chicken", "expiration_date": datetime.date(2022, 2, 5),  "price": 120},
    {"name": "duck",    "expiration_date": datetime.date(2022, 2, 1),  "price": 160},
]


@pytest.fixture
def freeze_date():
    real_date = datetime.date

    with mock.patch("app.main.datetime.date") as mocked_date:
        mocked_date.side_effect = lambda *a, **kw: real_date(*a, **kw)

        def _set(d):
            mocked_date.today.return_value = d

        yield _set


def test_only_duck_outdate(freeze_date):
    freeze_date(datetime.date(2022, 2, 2))
    assert outdated_products(products) == ["duck"]


def test_duck_and_chicken_outdate(freeze_date):
    freeze_date(datetime.date(2022, 2, 6))
    assert outdated_products(products) == ["chicken", "duck"]

def test_all_outdate(freeze_date):
    freeze_date(datetime.date(2022, 2, 11))
    assert outdated_products(products) == ["salmon", "chicken", "duck"]

def test_not_outdate_and_today_equal_date(freeze_date):
    freeze_date(datetime.date(2022, 2, 1))
    assert outdated_products(products) == []


