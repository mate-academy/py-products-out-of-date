import pytest
from datetime import date
from unittest import mock

from app.main import outdated_products


class TestOutdated:
    @pytest.mark.parametrize(
        "products, expected_outdated",
        [
            pytest.param(
                [
                    {
                        "name": "salmon",
                        "expiration_date": date(2022, 2, 10),
                        "price": 600
                    },
                    {
                        "name": "chicken",
                        "expiration_date": date(2022, 2, 5),
                        "price": 120
                    },
                    {
                        "name": "duck",
                        "expiration_date": date(2022, 2, 1),
                        "price": 160
                    }
                ],
                ["duck"],
                id="test_outdated_exist"
            ),
            pytest.param(
                [
                    {
                        "name": "salmon",
                        "expiration_date": date(2022, 2, 10),
                        "price": 600
                    },
                    {
                        "name": "chicken",
                        "expiration_date": date(2022, 2, 5),
                        "price": 120
                    },
                    {
                        "name": "duck",
                        "expiration_date": date(2022, 2, 8),
                        "price": 160
                    }
                ],
                [],
                id="test_no_outdated"
            ),
            pytest.param(
                [],
                [],
                id="test_empty_list"
            ),
            pytest.param(
                [
                    {
                        "name": "duck",
                        "expiration_date": date(2022, 2, 2),
                        "price": 160
                    }
                ],
                [],
                id="test_same_day_not_outdated"
            )
        ]
    )
    def test_outdated(
            self,
            products: list[dict],
            expected_outdated: list[str],
    ) -> None:
        with mock.patch(
            "app.main.datetime.date"
        ) as mocked_date:
            mocked_date.today.return_value = date(2022, 2, 2)
            assert outdated_products(products) == expected_outdated
