import pytest
import datetime
from unittest import mock
from app.main import outdated_products


@pytest.fixture(scope="module")
def products() -> list:
    return [
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
    ]


class TestOutdatedProducts:
    @pytest.mark.parametrize(
        "expected_result_list",
        [
            pytest.param(
                ["duck"],
                id="should return duck product name cause date is expired"
            )
        ]
    )
    def test_should_return_names_of_expired_products(
            self,
            products: list,
            expected_result_list: list
    ) -> None:
        with mock.patch("app.main.datetime") as mock_today_date:
            mock_today_date.date.today.return_value = datetime.date(2022, 2, 2)
            assert outdated_products(products) == expected_result_list
