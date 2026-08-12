import datetime
from unittest import mock

from app.main import outdated_products


@mock.patch("app.main.datetime")
def test_should_return_out_of_date(mocked_date: mock.MagicMock) -> None:
    products = [
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

    mocked_date.date.today.return_value = datetime.date(2022, 2, 2)

    assert outdated_products(products) == ["duck"]
