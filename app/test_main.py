from unittest import mock

import datetime

from app.main import outdated_products


@mock.patch("app.main.datetime")
def test_checking_outdated_products(mocked_datetime: mock.Mock) -> None:
    mocked_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 2),
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
        }
    ]
    assert outdated_products(products) == ["salmon", "duck"]
