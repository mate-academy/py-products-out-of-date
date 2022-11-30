from datetime import date
from unittest import mock
from app.main import outdated_products

list_of_products = [
    {
        "name": "milk",
        "expiration_date": date(2022, 11, 20),
        "price": 40
    },
    {
        "name": "eggs",
        "expiration_date": date(2022, 11, 28),
        "price": 70
    },
    {
        "name": "meat",
        "expiration_date": date(2022, 12, 10),
        "price": 170
    }
]


@mock.patch("app.main.datetime")
def test_func(mock_date: mock) -> None:
    mock_date.date.today.return_value = date(2022, 11, 25)
    assert outdated_products(list_of_products) == ["milk"]
