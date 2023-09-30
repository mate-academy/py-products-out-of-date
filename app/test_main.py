import unittest
from app.main import outdated_products
from datetime import date
from unittest.mock import patch


class TestOutdatedProducts(unittest.TestCase):

    def test_no_outdated_products(self) -> None:
        products = [
            {
                "name": "salmon",
                "expiration_date": date(2022, 2, 15),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": date(2022, 3, 5),
                "price": 120
            }
        ]
        with patch("datetime.date") as mock_date:
            mock_date.today.return_value = date(2022, 2, 2)
            result = outdated_products(products)
            self.assertEqual(result, [])

    def test_some_outdated_products(self) -> None:
        products = [
            {
                "name": "salmon",
                "expiration_date": date(2022, 2, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": date(2022, 2, 5),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": date(2022, 2, 1),
                "price": 160
            }
        ]
        with patch("datetime.date") as mock_date:
            mock_date.today.return_value = date(2022, 2, 2)
            result = outdated_products(products)
            self.assertEqual(result, ["duck"])


if __name__ == "__main__":
    unittest.main()
