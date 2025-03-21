import unittest
import datetime
from typing import Any
from unittest.mock import patch, Mock

from app.main import outdated_products


@patch("app.main.datetime")
class TestOutdatedProducts(unittest.TestCase):
    def test_outdated_products(self, mock_today: Any) -> None:

        mock_today.date.today = Mock(return_value=datetime.date(2026, 1, 21))
        products = [
            {
                "name": "Milk",
                "expiration_date": datetime.date(2026, 1, 20),
                "price": 100
            },
            {
                "name": "Eggs",
                "expiration_date": datetime.date(2027, 3, 22),
                "price": 100
            },
            {
                "name": "Cheese",
                "expiration_date": datetime.date(2021, 3, 15),
                "price": 100
            },
        ]

        expected = ["Milk", "Cheese"]
        self.assertEqual(outdated_products(products), expected)

    def test_no_outdated_products(self, mock_today: Any) -> None:
        mock_today.date.today = Mock(return_value=datetime.date(2026, 1, 21))

        products = [
            {
                "name": "Bread",
                "expiration_date": datetime.date(2026, 3, 22),
                "price": 100
            },
            {
                "name": "Juice",
                "expiration_date": datetime.date(2026, 3, 25),
                "price": 100
            },
        ]

        self.assertEqual(outdated_products(products), [])


if __name__ == "__main__":
    unittest.main()
