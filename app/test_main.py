import datetime

from app.main import outdated_products
from unittest import mock

import pytest


class TestOutdatedProducts:
    @pytest.fixture
    def products(self) -> list:
        return [
            {
                "name": "product1",
                "expiration_date": datetime.date(2024, 10, 1),
                "price": 100
            },
            {
                "name": "product2",
                "expiration_date": datetime.date(2024, 10, 9),
                "price": 250
            },
            {
                "name": "product3",
                "expiration_date": datetime.date(2025, 7, 24),
                "price": 100
            }
        ]

    @mock.patch("app.main.datetime")
    def test_outdated_products(self,
                               mocked_datetime: mock,
                               products: list[dict]) -> None:
        mocked_datetime.date.today.return_value = datetime.date(2024, 10, 10)
        assert outdated_products(products) == ["product1", "product2"]
