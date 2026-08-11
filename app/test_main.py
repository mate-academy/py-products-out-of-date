import datetime
import unittest
from unittest import mock

import app.main as main


class FakeDate(datetime.date):
    @classmethod
    def today(cls) -> datetime.date:
        return datetime.date(2023, 1, 1)


class TestOutdatedProducts(unittest.TestCase):
    @mock.patch("app.main.datetime.date", FakeDate)
    def test_outdated_products(self) -> None:
        products = [
            {"name": "Milk", "expiration_date": datetime.date(2022, 12, 31)},
            {"name": "Bread", "expiration_date": datetime.date(2023, 1, 2)},
            {"name": "Cheese", "expiration_date": datetime.date(2023, 1, 1)},
        ]
        expected = ["Milk"]
        result = main.outdated_products(products)
        self.assertEqual(result, expected)
