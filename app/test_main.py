from app.main import outdated_products
import datetime
import pytest


@pytest.fixture
def list_products():
    return ([{
        "name": "salmon",
        "expiration_date": datetime.date(2022, 8, 6),
        "price": 600},
        {
        "name": "chicken",
        "expiration_date": datetime.date(2022, 8, 19),
        "price": 120},
        {
        "name": "duck",
        "expiration_date": datetime.date(2022, 9, 2),
        "price": 160
      }])


def test_expiration_all_dates_less_date(list_products):
    # change date
    list_products[0]["expiration_date"] = datetime.date(2022, 7, 31)
    list_products[1]["expiration_date"] = datetime.date(2022, 7, 15)
    list_products[2]["expiration_date"] = datetime.date(2022, 6, 1)
    assert outdated_products(list_products) == ["salmon", "chicken", "duck"]


def test_expiration_all_dates_norm_date(list_products):
    list_products[0]["expiration_date"] = datetime.date(2022, 8, 24)
    list_products[1]["expiration_date"] = datetime.date(2022, 8, 19)
    list_products[2]["expiration_date"] = datetime.date(2022, 8, 30)
    assert outdated_products(list_products) == []


def test_expiration_dates_are_different_date(list_products):
    list_products[0]["expiration_date"] = datetime.date(2022, 7, 12)
    list_products[1]["expiration_date"] = datetime.date(2022, 8, 19)
    list_products[2]["expiration_date"] = datetime.date(2022, 9, 30)
    assert outdated_products(list_products) == ["salmon"]
