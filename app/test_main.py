import pytest
from unittest import mock
from app.main import outdated_products
import datetime


class TestOutdatedProducts:
    @mock.patch("app.main.datetime")
    @pytest.mark.parametrize(
        "date,expected_result",
        [
            (datetime.date(2022, 2, 2), ['duck']),
            (datetime.date(2022, 2, 6), ['chicken', 'duck']),
            (datetime.date(2022, 2, 10), ['chicken', 'duck']),
            (datetime.date(2022, 2, 11), ['salmon', 'chicken', 'duck'])
        ]
    )
    def test_should_return_valid_values(self,
                                        mocked_datetime,
                                        date,
                                        expected_result):
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
        mocked_datetime.date.today.return_value = date
        assert outdated_products(products) == expected_result
