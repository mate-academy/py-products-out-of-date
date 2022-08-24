from unittest import mock
import datetime
import pytest
from app.main import outdated_products


class Test:
    @mock.patch("app.main.datetime")
    @pytest.mark.parametrize(
        "products, expected_result", [
            (
                [
                    {
                        "name": "salmon",
                        "expiration_date": datetime.date(2022, 2, 10),
                        "price": 600
                    },
                    {
                        "name": "chicken",
                        "expiration_date": datetime.date(2022, 8, 23),
                        "price": 120
                    },
                    {
                        "name": "duck",
                        "expiration_date": datetime.date(2022, 8, 24),
                        "price": 160
                    }
                ],
                ['salmon', 'chicken']
            )
        ]
    )
    def test_outdated_prods(self, mock_date, products, expected_result):

        mock_date.date.today = \
            mock.Mock(return_value=datetime.date(2022, 8, 24))
        assert outdated_products(products) == expected_result
