from unittest import mock
from datetime import date
from app.main import outdated_products

product_list = [
    {
        "name": "salmon",
        "expiration_date": date(2022, 2, 10),
        "price": 600
    },
    {
        "name": "chicken",
        "expiration_date": date(2022, 2, 5),
        "price": 120
    },
    {
        "name": "duck",
        "expiration_date": date(2022, 2, 1),
        "price": 160
    }
]


@mock.patch("app.main.datetime")
def test_date_should_be_right(mocked_time: mock) -> None:
    mocked_time.date.today.return_value = date(2022, 2, 2)
    assert outdated_products(product_list) == ["duck"]
