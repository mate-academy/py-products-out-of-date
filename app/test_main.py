import unittest
import datetime

from unittest.mock import patch

from app.main import outdated_products


class TestOutdatedProducts(unittest.TestCase):

    @patch("app.main.datetime")
    def test_outdated_products(self, mock_datetime: datetime) -> None:
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

        self.assertEqual(outdated_products(products), ["duck"])
