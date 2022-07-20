from unittest import mock
import app.main

import datetime
import pytest


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


class TestOutdatedProduct:
    @pytest.mark.parametrize(
        "date, result",
        [
            pytest.param(
                datetime.date(2022, 1, 1),
                [],
                id="All products are not outdated"
            ),
            pytest.param(
                datetime.date(2022, 2, 4),
                ["duck"],
                id="One product is outdated"
            ),
            pytest.param(
                datetime.date(2022, 3, 1),
                ["salmon", "chicken", "duck"],
                id="All products are outdated"
            )
        ]
    )
    @mock.patch("app.main.datetime", wraps=datetime)
    def test_outdated_products_works(
            self,
            mocked_datetime,
            date,
            result,
    ):
        mocked_datetime.date.today.return_value = date
        assert app.main.outdated_products(products) == result
