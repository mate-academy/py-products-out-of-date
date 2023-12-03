import pytest
import datetime
from unittest import mock
from typing import List

from app.main import outdated_products


class TestOutdatedProducts:

    @pytest.fixture()
    def mocked_today(self) -> None:
        with mock.patch("app.main.datetime") as date_mock:
            date_mock.date.today.return_value = datetime.date(2022, 2, 2)
            yield

    @pytest.mark.parametrize(
        "products,expected_outdated_product",
        [
            pytest.param(
                [
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
                ],
                ["duck"],
                id='Should return ["duck"]'
            ),
            pytest.param(
                [
                    {
                        "name": "salmon",
                        "expiration_date": datetime.date(2024, 2, 10),
                        "price": 600
                    },
                    {
                        "name": "chicken",
                        "expiration_date": datetime.date(2024, 2, 5),
                        "price": 120
                    },
                    {
                        "name": "duck",
                        "expiration_date": datetime.date(2024, 2, 1),
                        "price": 160
                    }
                ],
                [],
                id="when all products fresh should return an empty list"
            ),
            pytest.param(
                [],
                [],
                id="when the list is empty, it should return an empty list"
            )
        ]
    )
    def test_outdated_products(
        self,
        products: List[dict],
        expected_outdated_product: List[str],
        mocked_today: None
    ) -> None:
        assert outdated_products(products) == expected_outdated_product
