import unittest
import datetime
from unittest.mock import patch

from app.main import outdated_products


class TestOutdatedProducts(unittest.TestCase):
    def test_empty_list(self) -> None:
        with patch("app.main.datetime") as mock_datetime:
            # Mock the datetime.date.today() method to return a fixed date
            mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
            self.assertEqual(outdated_products([]), [])

    def test_no_outdated_products(self) -> list:
        with patch("app.main.datetime") as mock_datetime:
            mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
            products = [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2023, 12, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2023, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2023, 3, 1),
                    "price": 160
                }
            ]
            self.assertEqual(outdated_products(products), [])

    def test_some_outdated_products(self) -> list:
        with patch("app.main.datetime") as mock_datetime:
            mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
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
            self.assertEqual(outdated_products(products),
                             ["duck"])


if __name__ == "__main__":
    unittest.main()
