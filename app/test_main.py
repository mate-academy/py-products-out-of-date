from typing import Any
from unittest import TestCase, mock
import datetime


from app.main import outdated_products


actual_date = datetime.date


@mock.patch("app.main.datetime.date")
class TestOutdatedProducts(TestCase):
    def test_outdated_products(self, mocked_date: Any) -> None:
        mocked_date.today.return_value = actual_date(2022, 2, 2)
        mocked_date.side_effect = lambda *args, **kwargs: (
            actual_date(*args, **kwargs))
        assert outdated_products([
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
            },
            {
                "name": "meat",
                "expiration_date": datetime.date(2022, 2, 2),
                "price": 160
            }
        ]) == ["duck"]
