from unittest.mock import Mock, patch
import unittest
import datetime


from app.main import outdated_products


class TestOutdatedProducts(unittest.TestCase):

    @patch("app.main.datetime")
    def test_outdated_products(self, mock_datetime: Mock) -> None:
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

        outdated = outdated_products(products)
        self.assertEqual(outdated, ["duck"])


if __name__ == "__main__":
    unittest.main()
