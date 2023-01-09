import datetime
from datetime import date

from app.main import outdated_products

from unittest import mock

import pytest


class TestOutdatedProducts:
    test_list = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 4, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 3, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]

    @pytest.mark.parametrize(
        "today_date, expired_products",
        [
            (date(2023, 1, 1), ["salmon", "chicken", "duck"]),
            (date(2022, 1, 1), []),
            (date(2022, 2, 2), ["duck"]),
            (date(2022, 4, 10), ["chicken", "duck"]),
        ]
    )
    @mock.patch("app.main.datetime")
    def test_outdated_products(
            self,
            mocked_datetime: callable,
            today_date: tuple,
            expired_products: list
    ) -> None:
        mocked_datetime.date.today.return_value = today_date
        assert outdated_products(self.test_list) == expired_products
