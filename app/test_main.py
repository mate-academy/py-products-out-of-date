import pytest
import datetime

from unittest.mock import patch
from app.main import outdated_products


class TestOutdatedProducts:
    @pytest.mark.parametrize("products, outdated_product", [([
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
        }], "duck")])
    @patch("app.main.datetime")
    def test_outdated_products(self,
                               mock_time: any,
                               products: list,
                               outdated_product: list) -> None:

        mock_time.date.today.return_value = datetime.date(2022, 2, 2)

        result = outdated_products(products)

        assert result == outdated_product
