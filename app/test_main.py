from unittest import TestCase
from unittest.mock import patch, MagicMock
from app.main import outdated_products
import datetime


class TestOutdatedProducts(TestCase):

    @patch("app.main.datetime")
    def test_outdated_products_no_outdated_products(
            self,
            datetime_mock: MagicMock
    ) -> None:
        datetime_mock.date.today.return_value = datetime.date(2022, 2, 2)

        products = [
            {"name": "salmon",
             "expiration_date": datetime.date(2022, 2, 10),
             "price": 600},
            {"name": "chicken",
             "expiration_date": datetime.date(2022, 2, 5),
             "price": 120},
        ]
        self.assertEqual(outdated_products(products), [])

    @patch("app.main.datetime")
    def test_outdated_products_some_outdated_products(
            self,
            datetime_mock: MagicMock
    ) -> None:
        datetime_mock.date.today.return_value = datetime.date(2022, 2, 2)
        products = [
            {"name": "salmon",
             "expiration_date": datetime.date(2022, 2, 10),
             "price": 600},
            {"name": "chicken",
             "expiration_date": datetime.date(2022, 2, 5),
             "price": 120},
            {"name": "duck",
             "expiration_date": datetime.date(2022, 1, 30),
             "price": 160},
        ]
        self.assertEqual(outdated_products(products), ["duck"])
