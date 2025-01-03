from unittest import mock
import datetime

from app.main import outdated_products


def test_outdated_product() -> None:
    store = [
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
    with mock.patch("app.main.datetime") as mocked_date:
        mocked_date.date.today.return_value = datetime.date(2022, 2, 6)
        assert (
            outdated_products(store) == ["chicken", "duck"]
        )
