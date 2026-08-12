import datetime
from unittest import mock

from app.main import outdated_products


@mock.patch("app.main.datetime", create=True)
def test_outdated_products(mock_datetime: mock.MagicMock) -> list:
    mock_datetime.date.today.return_value = datetime.date(2022, 2, 3)

    test_products = [
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

    assert outdated_products(test_products) == ["duck"]

    test_products_no_outdated = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        }
    ]
    assert outdated_products(test_products_no_outdated) == []
