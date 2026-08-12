import datetime

from app.main import outdated_products

from unittest import mock


@mock.patch("app.main.datetime")
def test_outdated_products(mocked_datetime: mock.MagicMock) -> None:
    products = [
        {"name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600},

        {"name": "chicken",
         "expiration_date": datetime.date(2022, 2, 5),
         "price": 120},

        {"name": "duck",
         "expiration_date": datetime.date(2022, 2, 1),
         "price": 160},
    ]

    mocked_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    mocked_datetime.date.side_effect = datetime.date
    assert outdated_products(products) == ["duck"]

    mocked_datetime.date.today.return_value = datetime.date(2022, 2, 11)
    assert outdated_products(products) == ["salmon", "chicken", "duck"]

    mocked_datetime.date.today.return_value = datetime.date(2022, 1, 31)
    assert outdated_products(products) == []
