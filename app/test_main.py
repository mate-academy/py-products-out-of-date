import unittest
from unittest.mock import patch
import datetime
from app.main import outdated_products


class TestOutdatedProducts(unittest.TestCase):
    @patch("app.main.datetime")
    def test_outdated_products(self, mock_datetime: callable) -> None:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 2)
        mock_datetime.date.side_effect = datetime.date

        products = [
            {"name": "Pork", "expiration_date": datetime.date(2022, 1, 20)},
            {"name": "Duck", "expiration_date": datetime.date(2022, 2, 3)},
            {"name": "Butter", "expiration_date": datetime.date(2022, 2, 1)}
        ]

        result = outdated_products(products)
        self.assertIn("Butter", result)
        self.assertNotIn("Duck", result)
