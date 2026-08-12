import datetime
from unittest import TestCase, mock

from app.main import outdated_products


class TestProducts(TestCase):
    def setUp(self) -> None:
        self.products = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2024, 12, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2024, 12, 5),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2024, 12, 1),
                "price": 160
            }
        ]

    def tearDown(self) -> None:
        del self.products

    @mock.patch("app.main.datetime")
    def test_should_return_list_of_products_with_expired_day(
            self,
            mock_today: mock
    ) -> None:
        mock_today.date.today.return_value = datetime.date(2024, 12, 4)
        assert outdated_products(self.products) == ["duck"]
