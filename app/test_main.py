from datetime import date
from unittest import mock
from app.main import outdated_products


@mock.patch("datetime.date")
def test_outdated_products(mocked_date: mock) -> None:
    mocked_date.today.return_value = date(2022, 2, 2)

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
        },
        {
            "name": "cheese",
            "expiration_date": date(2022, 2, 2),
            "price": 200
        }
    ]

    assert outdated_products(product_list) == ["duck"]
