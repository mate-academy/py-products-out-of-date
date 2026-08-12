from unittest.mock import patch

from app.main import outdated_products


class TestOutdatedProducts:

    @patch("app.main.datetime")
    def test_outdated_products(self, mock_datetime: patch) -> None:
        mock_datetime.date.today.return_value = "2020-10-10"
        products = [
            {"name": "Product 1", "expiration_date": "2020-10-09"},
            {"name": "Product 2", "expiration_date": "2020-10-10"},
            {"name": "Product 3", "expiration_date": "2020-10-11"},
        ]
        assert outdated_products(products) == ["Product 1"]
