import datetime
from unittest import mock

from app.main import outdated_products


list_of_products = [
    {
        "name": "salmon",
        "expiration_date": datetime.date(2027, 2, 10),
        "price": 600
    },
    {
        "name": "chicken",
        "expiration_date": datetime.date(2027, 2, 5),
        "price": 120
    },
    {
        "name": "duck",
        "expiration_date": datetime.date(2015, 2, 1),
        "price": 160
    }
]


@mock.patch("app.main.datetime")
def test_if_date_equal_today(mocked_datetime: object) -> None:
    mocked_datetime.date.today.return_value = datetime.date(2015, 2, 1)

    assert (
        outdated_products(list_of_products)
        == []
    )


@mock.patch("app.main.datetime")
def test_should_nothing_is_be_expired(mocked_datetime: object) -> None:
    mocked_datetime.date.today.return_value = datetime.date(2000, 1, 1)

    assert (
        outdated_products(list_of_products)
        == []
    )


@mock.patch("app.main.datetime")
def test_should_all_be_expired(mocked_datetime: mock) -> None:
    mocked_datetime.date.today.return_value = datetime.date(2030, 2, 2)

    assert (
        outdated_products(list_of_products)
        == ["salmon", "chicken", "duck"]
    )
