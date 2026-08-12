import unittest
from unittest.mock import patch
import datetime

from app.main import outdated_products


class TestOutdatedProducts(unittest.TestCase):
    @patch("app.main.datetime")
    def test_outdated_products(self, mock_datetime: datetime) -> any:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 5)

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

        expected = ["duck"]

        result = outdated_products(products)
        self.assertEqual(result, expected)

    @patch("app.main.datetime")
    def test_no_outdated_products(self, mock_datetime: datetime) -> any:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 1)

        products = [
            {"name": "salmon",
             "expiration_date": datetime.date(2022, 2, 10),
             "price": 600},
            {"name": "chicken",
             "expiration_date": datetime.date(2022, 2, 5),
             "price": 120},
        ]

        expected = []
        result = outdated_products(products)
        self.assertEqual(result, expected)

    @patch("app.main.datetime")
    def test_all_outdated_products(self, mock_datetime: datetime) -> any:
        mock_datetime.date.today.return_value = datetime.date(2022, 3, 1)

        products = [
            {"name": "salmon",
             "expiration_date": datetime.date(2022, 2, 10),
             "price": 600},
            {"name": "chicken",
             "expiration_date": datetime.date(2022, 2, 5),
             "price": 120},
        ]

        expected = ["salmon", "chicken"]
        result = outdated_products(products)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
