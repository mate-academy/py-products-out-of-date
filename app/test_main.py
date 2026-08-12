import datetime

from unittest import TestCase
from unittest.mock import patch

from app.main import outdated_products


class TestOutdatedProducts(TestCase):
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
        result = outdated_products(products)
        self.assertEqual(result, ["duck"])
