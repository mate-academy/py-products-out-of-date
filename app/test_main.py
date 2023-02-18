import datetime
from unittest import mock
from app.main import outdated_products

list_of_products = [
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
def test_should_return_empty_list_if_expiration_date_equal_today(
        mocked_date: mock) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 2, 1)
    assert outdated_products(list_of_products) == []


@mock.patch("app.main.datetime")
def test_should_return_list_with_all_products_if_expiration_date_lt_actual(
        mocked_date: mock) -> None:
    mocked_date.date.today.return_value = datetime.date(2022, 2, 11)
    assert outdated_products(list_of_products) == ["salmon", "chicken", "duck"]
