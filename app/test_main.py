import unittest
from unittest.mock import patch, MagicMock
import datetime
from app.main import outdated_products


class TestOutdatedProducts(unittest.TestCase):
    @patch("app.main.datetime")
    def test_no_outdated_products(self, mock_datetime: MagicMock) -> None:
        # Mock today's date
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
            }
        ]
        self.assertEqual(outdated_products(products), [])

    @patch("app.main.datetime")
    def test_some_outdated_products(self, mock_datetime: MagicMock) -> None:
        # Mock today's date
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)

        products = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 1),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 1, 30),
                "price": 160
            }
        ]
        self.assertEqual(outdated_products(products), ["chicken", "duck"])

    @patch("app.main.datetime")
    def test_all_outdated_products(self, mock_datetime: MagicMock) -> None:
        # Mock today's date
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)

        products = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 1, 31),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 1, 25),
                "price": 120
            }
        ]
        self.assertEqual(outdated_products(products), ["salmon", "chicken"])

    @patch("app.main.datetime")
    def test_empty_product_list(self, mock_datetime: MagicMock) -> None:
        # Mock today's date
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)

        products = []
        self.assertEqual(outdated_products(products), [])


if __name__ == "__main__":
    unittest.main()
