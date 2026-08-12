import datetime
from unittest import mock
from app.main import outdated_products


@mock.patch("app.main.datetime.time")
def test_should_check_outdated_products(mocked_date: datetime) -> None:
    mocked_date.today.return_value = datetime.date(2023, 7, 12)
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2023, 7, 12),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2023, 7, 11),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]

    assert outdated_products(products) == ["chicken", "duck"]
