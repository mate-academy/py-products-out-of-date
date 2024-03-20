import datetime
from unittest.mock import patch, MagicMock

from app.main import outdated_products


class TestOutdatedProducts:

    @patch("app.main.datetime")
    def test_expected_result(self, mock_today: MagicMock) -> None:
        products = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 10),
                "price": 600,
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 5),
                "price": 120,
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 2, 1),
                "price": 160,
            },
        ]
        mock_today.date.today.return_value = datetime.date(2022, 2, 2)
        assert outdated_products(products) == ["duck"]
