import unittest

from unittest.mock import patch, Mock

from app.main import outdated_products

import datetime


class TestOutdatedProducts(unittest.TestCase):

    @patch("app.main.datetime")
    def test_outdated_products(self, mock_datetime: any) -> None:

        mock_today = Mock(return_value=datetime.date(2022, 2, 2))
        mock_datetime.date.today = mock_today

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

        result = outdated_products(products)
        self.assertEqual(result, ["duck"])

    @patch("app.main.datetime")
    def test_outdated_products_no_outdated(self, mock_datetime: any) -> None:

        mock_today = Mock(return_value=datetime.date(2022, 2, 2))
        mock_datetime.date.today = mock_today

        products = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 15),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 2, 20),
                "price": 160
            }
        ]

        result = outdated_products(products)
        self.assertEqual(result, [])
