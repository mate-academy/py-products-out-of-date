from unittest import mock
from app.main import outdated_products
import datetime

product_list = [
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
def test_check_current_date(mock_date: mock) -> None:

    mock_date.date.today.return_value = datetime.date(2022, 1, 1)

    assert outdated_products(product_list) == []


@mock.patch("app.main.datetime")
def test_check_all_date_out(mock_date: mock) -> None:

    mock_date.date.today.return_value = datetime.date(2022, 3, 1)

    assert outdated_products(product_list) == ["salmon", "chicken", "duck"]


@mock.patch("app.main.datetime")
def test_check_one_date_out(mock_date: mock) -> None:
    mock_date.date.today.return_value = datetime.date(2022, 2, 2)

    assert outdated_products(product_list) == ["duck"]
