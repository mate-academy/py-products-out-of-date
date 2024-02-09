import datetime
from unittest import mock

from app.main import outdated_products


class TestOutdatedProduct():

    def test_outdated_products_yesterday(self) -> None:
        with mock.patch("app.main.datetime") as mock_date:
            mock_date.date.today.return_value = datetime.date(2024, 2, 10)
            product = [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2024, 2, 9),
                    "price": 600
                }
            ]
            assert outdated_products(product) == ["salmon"]

    def test_outdated_products_today(self) -> None:
        with mock.patch("app.main.datetime") as mock_date:
            mock_date.date.today.return_value = datetime.date(2024, 2, 10)
            product = [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2024, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2024, 2, 5),
                    "price": 120
                }
            ]
            assert outdated_products(product) == ["salmon", "chicken"]
