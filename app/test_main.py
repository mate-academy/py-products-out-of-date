from unittest import TestCase, mock
from app.main import outdated_products
import datetime


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


class MockDate(datetime.date):
    @classmethod
    def today(cls) -> datetime.date:
        return cls._today


class TestOutdatedProducts(TestCase):
    @mock.patch("app.main.datetime.date", new=MockDate)
    def test_expiration_less(self) -> None:
        MockDate._today = datetime.date(2023, 1, 1)
        self.assertEqual(outdated_products(products),
                         ["salmon", "chicken", "duck"])

    @mock.patch("app.main.datetime.date", new=MockDate)
    def test_expiration_great(self,) -> None:
        MockDate._today = datetime.date(2021, 1, 1)
        self.assertEqual(outdated_products(products),
                         [])

    @mock.patch("app.main.datetime.date", new=MockDate)
    def test_expiration_different(self) -> None:
        MockDate._today = datetime.date(2022, 2, 5)
        self.assertEqual(outdated_products(products),
                         ["duck"])

    @mock.patch("app.main.datetime.date", new=MockDate)
    def test_expiration_yesterday(self) -> None:
        MockDate._today = datetime.date(2022, 2, 2)
        self.assertEqual(outdated_products(products),
                         ["duck"])
