import unittest
from unittest.mock import patch
import datetime

from app.main import outdated_products


class TestOutdatedProducts(unittest.TestCase):

    @patch("app.main.datetime")
    def test_outdated_products(self, mock_datetime: any) -> None:
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
            },
        ]
        result = outdated_products(products)
        self.assertEqual(result, ["duck"])

        products = [
            {
                "name": "apple",
                "expiration_date": datetime.date(2022, 2, 15),
                "price": 2
            },
            {
                "name": "banana",
                "expiration_date": datetime.date(2022, 2, 20),
                "price": 1
            },
        ]
        result = outdated_products(products)
        self.assertEqual(result, [])

        result = outdated_products([])
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
