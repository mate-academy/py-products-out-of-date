import datetime
import pytest

from app.main import outdated_products
from unittest.mock import patch


class TestOutdatedProductsClass:

    @pytest.fixture()
    def list_fixture(self) -> list:
        outdated_products_list = [
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
        return outdated_products_list

    @pytest.mark.parametrize(
        "modified_name, expected_result",
        [
            ("keki4", ["keki4", "chicken", "duck"]),
            ("salmon", ["salmon", "chicken", "duck"]),
        ],
    )
    def test_outdated_products_with_variations(self,
                                               list_fixture: list,
                                               modified_name: str,
                                               expected_result: list
                                               ) -> None:
        list_fixture[0]["name"] = modified_name
        assert outdated_products(list_fixture) == expected_result


class TestOutdatedProductsVariationsTime:
    @pytest.fixture
    def list_fixture(self) -> list:
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

    @patch("app.main.datetime")
    def test_with_right_time(self,
                             datetime_mock: str,
                             list_fixture: list
                             ) -> None:
        datetime_mock.date.today.return_value = datetime.date(2021, 6, 1)
        assert outdated_products(list_fixture) == []

    @patch("app.main.datetime")
    def test_with_wrong_time(self,
                             datetime_mock: str,
                             list_fixture: list
                             ) -> None:
        datetime_mock.date.today.return_value = datetime.date(2023, 6, 1)
        assert outdated_products(list_fixture) == ["salmon", "chicken", "duck"]
