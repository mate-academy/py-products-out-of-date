import datetime
from unittest import mock, TestCase
from app.main import outdated_products


@mock.patch("app.main.datetime")
class TestApp(TestCase):
    def setUp(self) -> None:
        self.products = [
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

    def test_duck_out_of_date(self, mocked_date: mock) -> None:
        mocked_date.date.today.return_value = datetime.date(2022, 2, 2)
        assert outdated_products(self.products) == ["duck"]

    def test_chicken_and_duck_out_of_date(self, mocked_date: mock) -> None:
        mocked_date.date.today.return_value = datetime.date(2022, 2, 6)
        assert outdated_products(self.products) == ["chicken", "duck"]

    def test_all_products_out_of_date(self, mocked_date: mock) -> None:
        mocked_date.date.today.return_value = datetime.date(2022, 2, 11)
        assert outdated_products(self.products) == \
               ["salmon", "chicken", "duck"]
