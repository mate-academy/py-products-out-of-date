import pytest
from unittest import mock
from datetime import date
from typing import Callable

from app.main import outdated_products


class TestOutdatedProduct:
    @pytest.mark.parametrize(
        "dates,expected_result",
        [
            pytest.param(
                [
                    {
                        "name": "Milk",
                        "expiration_date": date(2023, 6, 10),

                    },
                    {
                        "name": "Apple",
                        "expiration_date": date(2023, 6, 10),
                    }
                ],
                ["Milk", "Apple"],
                id="The expiration date has passed"
            ),
            pytest.param(
                [
                    {
                        "name": "Milk",
                        "expiration_date": date(2023, 6, 12),

                    },
                    {
                        "name": "Apple",
                        "expiration_date": date(2023, 6, 15),

                    }
                ],
                ["Milk"],
                id="Choose only products name  that are out of date"
            ),
            pytest.param(
                [
                    {
                        "name": "Milk",
                        "expiration_date": date(2023, 6, 13),
                    },
                ],
                [],
                id="Last date inclusive"
            )
        ]
    )
    @mock.patch("datetime.date")
    def test_outdated_products(
            self,
            date_mock: Callable,
            dates: list,
            expected_result: list
    ) -> None:
        date_mock.today.return_value = date(2023, 6, 13)

        assert outdated_products(dates) == expected_result
