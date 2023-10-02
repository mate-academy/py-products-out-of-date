import unittest
from app.main import outdated_products
import datetime


class TestOutdatedProducts(unittest.TestCase):

    def test_empty_product_list(self) -> None:
        products = []
        result = outdated_products(products)
        self.assertEqual(result, [])

    def test_no_outdated_products(self) -> None:
        today = datetime.date.today()
        products = [
            {"name": "Product1", "expiration_date":
                today + datetime.timedelta(days=5)},
            {"name": "Product2", "expiration_date":
                today + datetime.timedelta(days=10)}
        ]
        result = outdated_products(products)
        self.assertEqual(result, [])

    def test_some_outdated_products(self) -> None:
        today = datetime.date.today()
        products = [
            {"name": "Product1", "expiration_date":
                today - datetime.timedelta(days=5)},
            {"name": "Product2", "expiration_date":
                today + datetime.timedelta(days=5)},
            {"name": "Product3", "expiration_date":
                today + datetime.timedelta(days=10)}
        ]
        result = outdated_products(products)
        self.assertEqual(result, ["Product1"])

    def test_all_outdated_products(self) -> None:
        today = datetime.date.today()
        products = [
            {"name": "Product1", "expiration_date":
                today - datetime.timedelta(days=5)},
            {"name": "Product2", "expiration_date":
                today - datetime.timedelta(days=1)}
        ]
        result = outdated_products(products)
        self.assertEqual(result, ["Product1", "Product2"])


if __name__ == "__main__":
    unittest.main()
