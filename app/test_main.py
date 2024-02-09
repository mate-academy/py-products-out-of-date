import datetime
from unittest import mock

from app.main import outdated_products


class TestOutdatedProduct():

    def test_expiration_day_yesterday_outdated(self) -> None:
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
                    "expiration_date": datetime.date(2024, 2, 9),
                    "price": 120
                },
            ]
            assert outdated_products(product) == ["chicken"]

    def test_expiration_day_today_not_outdated(self):
        product = [
            {
                "name": "salmon",
                "expiration_date": datetime.date.today(),
                "price": 600
            }
        ]
        assert outdated_products(product) == []
