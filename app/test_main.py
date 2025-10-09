from datetime import date

import pytest
from unittest import mock

from app.main import outdated_products


@pytest.fixture()
def get_products() -> list:
    return [
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
    ]


class TestOutdatedProducts:
    @pytest.mark.parametrize(
        "mocked_date_return_value,expected_result",
        [
            pytest.param(
                date(2022, 2, 11),
                ["salmon", "chicken", "duck"]
            ),
            pytest.param(
                date(2022, 2, 10),
                ["chicken", "duck"]
            ),
            pytest.param(
                date(2022, 2, 5),
                ["duck"]
            ),
            pytest.param(
                date(2022, 2, 1),
                []
            )
        ]
    )
    def test_outdated_products_returns_correct_list(
            self,
            mocked_date_return_value: date,
            expected_result: list,
            get_products: list
    ) -> None:
        with (
            mock.patch("app.main.date")
            as mocked_date
        ):
            mocked_date.today.return_value = mocked_date_return_value
            assert outdated_products(get_products) == expected_result
